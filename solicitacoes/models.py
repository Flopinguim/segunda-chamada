from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
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
    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    motivo = models.TextField()
    arquivo = models.FileField(upload_to='solicitacoes/%Y/%m/', blank=True, null=True, help_text='Arquivo comprobatório (opcional)')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    professor_responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes', null=True, blank=True)
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
    
    class Meta:
        ordering = ['-data_solicitacao']
