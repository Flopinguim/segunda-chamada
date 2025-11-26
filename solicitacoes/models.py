from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Perfil(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('coordenador', 'Coordenador'),
        ('secretaria', 'Secretaria'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"


class Disciplina(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

    class Meta:
        ordering = ['codigo']


class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]
    APPROVAL_CHOICES = STATUS_CHOICES

    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    motivo = models.TextField()
    arquivo = models.FileField(upload_to='solicitacoes/%Y/%m/', blank=True, null=True, help_text='Arquivo comprobatório (opcional)')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    coordenador_status = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pendente')
    coordenador_justificativa = models.TextField(blank=True)
    coordenador_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='aprovacoes_coordenador', null=True, blank=True)
    coordenador_data = models.DateTimeField(null=True, blank=True)

    secretaria_status = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pendente')
    secretaria_justificativa = models.TextField(blank=True)
    secretaria_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='aprovacoes_secretaria', null=True, blank=True)
    secretaria_data = models.DateTimeField(null=True, blank=True)

    professor_status = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pendente')
    professor_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='avaliacoes', null=True, blank=True)
    observacoes_professor = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.username} - {self.disciplina.nome} ({self.status})"

    @property
    def tem_arquivo(self):
        return bool(self.arquivo)

    @property
    def nome_arquivo(self):
        if self.arquivo:
            return self.arquivo.name.split('/')[-1]
        return None

    @property
    def prazo_expirado(self):
        return bool(self.data_limite and timezone.now() > self.data_limite)

    def notificar_aluno(self, mensagem):
        Notificacao.objects.create(user=self.aluno, solicitacao=self, mensagem=mensagem)

    def pode_avaliar(self, tipo_aprovador):
        if self.status != 'pendente' or self.prazo_expirado:
            return False

        if tipo_aprovador == 'coordenador':
            return self.coordenador_status == 'pendente'
        if tipo_aprovador == 'secretaria':
            return self.coordenador_status == 'aprovada' and self.secretaria_status == 'pendente'
        if tipo_aprovador == 'professor':
            return self.coordenador_status == 'aprovada' and self.secretaria_status == 'aprovada' and self.professor_status == 'pendente'
        return False

    def atualizar_status_final(self):
        if self.data_limite and timezone.now() > self.data_limite and self.status == 'pendente':
            self.status = 'rejeitada'
            if not self.observacoes_professor:
                self.observacoes_professor = 'Rejeitada automaticamente por expirar o prazo.'
            return

        etapas = [
            self.coordenador_status,
            self.secretaria_status,
            self.professor_status,
        ]

        if 'rejeitada' in etapas:
            self.status = 'rejeitada'
        elif all(status == 'aprovada' for status in etapas):
            self.status = 'aprovada'
            if not self.data_avaliacao:
                self.data_avaliacao = timezone.now()
        else:
            self.status = 'pendente'

    def registrar_decisao(self, tipo_aprovador, usuario, decisao, justificativa=''):
        agora = timezone.now()

        if tipo_aprovador == 'coordenador':
            self.coordenador_status = decisao
            self.coordenador_responsavel = usuario
            self.coordenador_justificativa = justificativa
            self.coordenador_data = agora
        elif tipo_aprovador == 'secretaria':
            self.secretaria_status = decisao
            self.secretaria_responsavel = usuario
            self.secretaria_justificativa = justificativa
            self.secretaria_data = agora
        elif tipo_aprovador == 'professor':
            self.professor_status = decisao
            self.professor_responsavel = usuario
            self.observacoes_professor = justificativa
            self.data_avaliacao = agora

        self.atualizar_status_final()
        self.save()
        return decisao

    class Meta:
        ordering = ['-data_solicitacao']


class Notificacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    lido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'Notificacao para {self.user.username} - {self.solicitacao_id}'
