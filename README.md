# 🚀 Sistema de Solicitação de Segunda Chamada

Sistema web desenvolvido em Django para gerenciar solicitações de segunda chamada de provas entre alunos e professores, com interface moderna e intuitiva.

![Django](https://img.shields.io/badge/Django-5.2.6-green)
![Python](https://img.shields.io/badge/Python-3.11.9-blue)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

## 📑 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Modelos de Dados](#-modelos-de-dados)
- [Sistema de Autenticação](#-sistema-de-autenticação)
- [Interfaces do Sistema](#-interfaces-do-sistema)
- [Funcionalidades Técnicas](#-funcionalidades-técnicas)
- [API e URLs](#-api-e-urls)
- [Como Usar](#-como-usar)
- [Estrutura de Arquivos](#-estrutura-de-arquivos)
- [Contribuição](#-contribuição)

## 🚀 Visão Geral

O **Sistema de Solicitação de Segunda Chamada** é uma aplicação web que digitaliza e automatiza o processo de solicitação de segunda chamada de provas em instituições de ensino. O sistema permite que alunos façam solicitações fundamentadas com documentos comprobatórios, enquanto professores podem avaliar e responder a essas solicitações de forma organizada.

### Principais Benefícios:
- 1. **Processo Digital**: Elimina papelada e burocracias físicas
- 2. **Rastreabilidade**: Histórico completo de todas as solicitações
- 3. **Organização**: Interface clara para alunos e professores
- 4. **Documentação**: Upload de arquivos comprobatórios
- 5. **Eficiência**: Agiliza o processo de avaliação

## 🔧 Funcionalidades

### Para Alunos:
- ✅ **Registro e Login** no sistema
- ✅ **Criar solicitações** de segunda chamada
- ✅ **Upload de arquivos** comprobatórios (atestados, documentos, etc.)
- ✅ **Buscar e filtrar** suas próprias solicitações
- ✅ **Acompanhar status** das solicitações (Pendente, Aprovada, Rejeitada)
- ✅ **Visualizar observações** dos professores
- ✅ **Dashboard personalizado** com resumo das solicitações

### Para Professores:
- ✅ **Login diferenciado** como professor
- ✅ **Visualizar solicitações pendentes** que precisam de avaliação
- ✅ **Aprovar ou rejeitar** solicitações
- ✅ **Adicionar observações** às avaliações
- ✅ **Visualizar arquivos** enviados pelos alunos
- ✅ **Histórico completo** de avaliações realizadas
- ✅ **Interface focada** em produtividade

## 🛠 Tecnologias Utilizadas

### Backend:
- **Django 5.2.6**: Framework web Python
- **Python 3.11.9**: Linguagem de programação
- **SQLite**: Banco de dados (desenvolvimento)
- **Django ORM**: Mapeamento objeto-relacional

### Frontend:
- **HTML5**: Estrutura das páginas
- **TailwindCSS 3.0**: Framework CSS utilitário
- **JavaScript Vanilla**: Funcionalidades interativas
- **FontAwesome 6.4.0**: Ícones profissionais

### Ferramentas de Desenvolvimento:
- **Virtual Environment**: Isolamento de dependências
- **Django Management Commands**: Comandos personalizados
- **Django Migrations**: Controle de versão do banco de dados

## 📂 Estrutura do Projeto

```
2Chamada/
├── .venv/                          # Ambiente virtual Python
├── media/                          # Arquivos enviados pelos usuários
├── solicitacoes/                   # Arquivos organizados por data
├── segunda_chamada/                # Configurações do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Configurações principais
│   ├── urls.py                     # URLs principais do projeto
│   └── wsgi.py
├── solicitacoes/                   # App principal
│   ├── management/                 # Comandos personalizados
│   │   └── commands/
│   │       └── popular_disciplinas.py
│   ├── migrations/                 # Migrações do banco
│   ├── static/                     # Arquivos estáticos
│   ├── templates/                  # Templates HTML
│   │   └── solicitacoes/
│   │       ├── avaliar_solicitacao.html
│   │       ├── dashboard_aluno.html
│   │       ├── dashboard_professor.html
│   │       ├── formulario.html
│   │       ├── login.html
│   │       └── registro.html
│   ├── admin.py                    # Configurações do Django Admin
│   ├── apps.py
│   ├── models.py                   # Modelos de dados
│   ├── tests.py
│   ├── urls.py                     # URLs do app
│   └── views.py                    # Lógica de negócio
├── db.sqlite3                      # Banco de dados SQLite
├── manage.py                       # Utilitário Django
└── README.md                       # Documentação
```

## 🛠️ Instalação e Configuração

### Pré-requisitos:
- Python 3.11.9 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonagem)

### Passo a passo:

1. **Clone o repositório** (ou baixe os arquivos):
```bash
git clone <url-do-repositorio>
cd 2Chamada
```

2. **Crie e ative um ambiente virtual**:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências**:
```bash
pip install django==5.2.6
```

4. **Configure o banco de dados**:
```bash
python manage.py migrate
```

5. **Popule com disciplinas de exemplo**:
```bash
python manage.py popular_disciplinas
```

6. **Crie um superusuário** (opcional):
```bash
python manage.py createsuperuser
```

7. **Execute o servidor**:
```bash
python manage.py runserver
```

8. **Acesse o sistema**: http://127.0.0.1:8000

## 🗂 Modelos de Dados

### 1. Perfil
Extende o modelo User do Django para definir tipos de usuário.

```python
class Perfil(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
```

**Funcionalidades:**
- 1. Diferencia alunos de professores
- 2. Campo matricula para identificação única
- 3. Relacionamento um-para-um com User

### 2. Disciplina
Representa as disciplinas disponíveis no sistema.

```python
class Disciplina(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
```

**Funcionalidades:**
- 1. 20 disciplinas de TI pré-cadastradas
- 2. Código único para identificação
- 3. Sistema de ativação/desativação
- 4. Descrição detalhada de cada disciplina

### 3. Solicitacao (Modelo Principal)
Núcleo do sistema, representa cada solicitação de segunda chamada.

```python
class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]
    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    motivo = models.TextField()
    arquivo = models.FileField(upload_to='solicitacoes/%Y/%m/', blank=True, null=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    professor_responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes', null=True, blank=True)
    observacoes_professor = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(null=True, blank=True)
```

**Funcionalidades Avançadas:**
- 1. **Upload de arquivos** organizados por ano/mês
- 2. **Propriedades customizadas** (`tem_arquivo`, `nome_arquivo`)
- 3. **Rastreamento temporal** (data solicitação/avaliação)
- 4. **Relacionamentos inteligentes** com lazy loading
- 5. **Sistema de status** com workflow definido

## 🔒 Sistema de Autenticação

### Registro de Usuários:
- **Campos obrigatórios**: username, nome, sobrenome, email, senha
- **Campo opcional**: matrícula (para alunos)
- **Tipo de usuário**: aluno ou professor
- **Validações**: senhas iguais, username único

### Login Inteligente:
```python
# Redirecionamento automático baseado no tipo de usuário
try:
    perfil = user.perfil
    if perfil.tipo == 'professor':
        return redirect('dashboard_professor')
    else:
        return redirect('dashboard_aluno')
except Perfil.DoesNotExist:
    return redirect('dashboard_aluno')
```

### Proteção de Rotas:
- **@login_required**: Todas as views protegidas
- **Verificação de tipo**: Alunos não acessam área de professor
- **Redirecionamento inteligente**: Usuários direcionados à área correta

## 🖥 Interfaces do Sistema

### 1. Tela de Login
- **Design moderno** com gradientes azuis
- **Campos validados** em tempo real
- **Links** para registro
- **Responsiva** para mobile

### 2. Dashboard do Aluno
**Funcionalidades:**
- 1. **Botão destacado** para nova solicitação
- 2. **Tabela completa** com todas as informações
- 3. **Busca em tempo real** por disciplina ou motivo
- 4. **Filtro por status** (Pendente, Aprovada, Rejeitada)
- 5. **Indicadores visuais** coloridos para status
- 6. **Links para arquivos** enviados
- 7. **Observações dos professores** visíveis

**Colunas da tabela:**
- ✅ Disciplina (nome e código)
- ✅ Motivo (truncado com reticências)
- ✅ Arquivo (link ou "Sem arquivo")
- ✅ Data de solicitação
- ✅ Status (com ícones e cores)
- ✅ Observações do professor

### 3. Dashboard do Professor
**Seção 1 - Solicitações Pendentes:**
- 🚨 **Destaque visual** com ícone de alerta
- ✅ **Informações do aluno** com avatar
- ✅ **Detalhes da solicitação**
- ✅ **Botão "Avaliar"** para cada item
- ✅ **Link para arquivos** enviados

**Seção 2 - Histórico de Avaliações:**
- ✅ **Lista completa** de avaliações realizadas
- ✅ **Status colorido** (aprovada/rejeitada)
- ✅ **Data de avaliação**
- ✅ **Interface limpa** sem filtros

### 4. Formulário de Nova Solicitação
- **Dropdown de disciplinas** com todas as opções
- **Campo de texto** expansível para motivo
- **Upload de arquivo** com drag & drop visual
- **Botões de ação** claramente definidos
- **Validação** no frontend e backend

### 5. Tela de Avaliação (Professor)
- **Informações completas** do aluno e solicitação
- **Visualização do arquivo** em nova aba
- **Botões de decisão** (Aprovar/Rejeitar)
- **Campo de observações** para feedback
- **Interface focada** na tomada de decisão

## ⚙️ Funcionalidades Técnicas

### 1. Sistema de Upload de Arquivos
```python
# Organização automática por data
arquivo = models.FileField(upload_to='solicitacoes/%Y/%m/', blank=True, null=True)

# Propriedades customizadas
@property
def tem_arquivo(self):
    return bool(self.arquivo)

@property
def nome_arquivo(self):
    if self.arquivo:
        return self.arquivo.name.split('/')[-1]
    return None
```

**Características:**
- 1. **Organização temporal**: Arquivos salvos em `/media/solicitacoes/YYYY/MM/`
- 2. **Validação automática**: Verificação de existência
- 3. **Nome limpo**: Extração do nome do arquivo
- 4. **Segurança**: Upload controlado pelo Django

### 2. Sistema de Busca Dinâmica (JavaScript)
```javascript
function filterTable() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedStatus = statusFilter.value.toLowerCase();

    tableRows.forEach(row => {
        const disciplina = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
        const motivo = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
        const status = row.querySelector('td:nth-child(5) span').textContent.toLowerCase();

        const matchesSearch = disciplina.includes(searchTerm) || motivo.includes(searchTerm);
        const matchesStatus = !selectedStatus || status.includes(selectedStatus);

        row.style.display = (matchesSearch && matchesStatus) ? '' : 'none';
    });
}
```

**Funcionalidades:**
- ⚡ **Busca instantânea**: Sem recarregamento de página
- ✅ **Múltiplos campos**: Busca em disciplina e motivo
- ✅ **Filtro por status**: Dropdown independente
- ✅ **Responsivo**: Funciona em mobile
- ✅ **Feedback visual**: Mensagem quando não há resultados

### 3. Management Command para Disciplinas
```python
# Comando: python manage.py popular_disciplinas
class Command(BaseCommand):
    help = 'Popula o banco com disciplinas de TI'
    
    def handle(self, *args, **options):
        disciplinas = [
            {'codigo': 'ALG001', 'nome': 'Algoritmos e Estruturas de Dados I', ...},
            # ... 19 outras disciplinas
        ]
        
        for disc_data in disciplinas:
            disciplina, created = Disciplina.objects.get_or_create(
                codigo=disc_data['codigo'],
                defaults={...}
            )
```

**Vantagens:**
- ✅ **Setup rápido**: 20 disciplinas criadas automaticamente
- ✅ **Idempotente**: Não duplica registros existentes
- ✅ **Conteúdo relevante**: Disciplinas de TI atuais
- ✅ **Feedback visual**: Mostra o que foi criado/já existia

## 🌐 API e URLs

### Estrutura de URLs:
```python
# segunda_chamada/urls.py (URLs principais)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solicitacoes.urls')),
    path('media/', serve_media_files),  # Servir arquivos em desenvolvimento
]

# solicitacoes/urls.py (URLs do app)
urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/aluno/', views.dashboard_aluno, name='dashboard_aluno'),
    path('dashboard/professor/', views.dashboard_professor, name='dashboard_professor'),
    path('nova-solicitacao/', views.nova_solicitacao, name='nova_solicitacao'),
    path('avaliar/<int:solicitacao_id>/', views.avaliar_solicitacao, name='avaliar_solicitacao'),
]
```

### Views Principais:

#### 1. `user_login` - Sistema de Login
- **Método**: GET (formulário), POST (autenticação)
- **Redirecionamento**: Baseado no tipo de usuário
- **Validação**: Username/password com feedback de erro

#### 2. `dashboard_aluno` - Dashboard do Aluno
- **Proteção**: @login_required
- **Dados**: Solicitações do usuário logado
- **Funcionalidade**: Busca e filtro via JavaScript

#### 3. `dashboard_professor` - Dashboard do Professor
- **Proteção**: @login_required + verificação de tipo
- **Dados**: Solicitações pendentes + histórico de avaliações
- **Separação**: Duas consultas otimizadas

#### 4. `nova_solicitacao` - Criar Solicitação
- **Proteção**: Apenas alunos
- **Upload**: Processamento de arquivos
- **Validação**: Campos obrigatórios + arquivo opcional

#### 5. `avaliar_solicitacao` - Avaliar (Professor)
- **Proteção**: Apenas professores
- **Dados**: Solicitação específica + arquivo
- **Ação**: Aprovar/rejeitar + observações

## 📚 Como Usar

### Para Alunos:

1. **Registrar-se**:
   - Acesse a página inicial
   - Clique em "Criar conta"
   - Preencha os dados (selecione "Aluno")
   - Faça login

2. **Fazer uma Solicitação**:
   - No dashboard, clique "Nova Solicitação"
   - Escolha a disciplina
   - Escreva o motivo detalhado
   - (Opcional) Anexe documento comprobatório
   - Clique "Enviar Solicitação"

3. **Acompanhar Status**:
   - Use a busca para encontrar solicitações específicas
   - Filtre por status (Pendente, Aprovada, Rejeitada)
   - Veja observações dos professores
   - Baixe seus arquivos enviados

### Para Professores:

1. **Registrar-se**:
   - Crie conta selecionando "Professor"
   - Faça login (será direcionado ao dashboard de professor)

2. **Avaliar Solicitações**:
   - Veja solicitações pendentes destacadas em amarelo
   - Clique "Avaliar" na solicitação desejada
   - Leia o motivo e baixe arquivos se houver
   - Escolha "Aprovar" ou "Rejeitar"
   - Adicione observações (opcional)
   - Confirme a avaliação

3. **Consultar Histórico**:
   - Veja suas avaliações anteriores
   - Histórico completo com datas
   - Status colorido para fácil identificação

## 🎨 Design e UX

### Paleta de Cores:
- **Azul Primário**: #3b82f6 (botões, links)
- **Azul Secundário**: #2563eb (hovers, destaques)
- **Verde**: #10b981 (aprovado, sucesso)
- **Amarelo**: #f59e0b (pendente, atenção)
- **Vermelho**: #ef4444 (rejeitado, erro)
- **Cinza**: #6b7280 (textos secundários)

### Componentes Reutilizáveis:
- **Cards com sombra**: Containers principais
- **Botões com gradiente**: CTAs importantes
- **Badges coloridas**: Status das solicitações
- **Ícones contextuais**: FontAwesome em toda interface
- **Tabelas responsivas**: Adaptam-se ao mobile

### Responsividade:
- **Desktop First**: Otimizado para telas grandes
- **Breakpoints**: sm, md, lg, xl do Tailwind
- **Mobile Friendly**: Tabelas scrolláveis horizontalmente
- **Touch Targets**: Botões com tamanho adequado para mobile

## 🗃 Estrutura de Arquivos Detalhada

### Templates (Frontend):
```
templates/solicitacoes/
├── login.html                 # Tela de login/entrada
├── registro.html              # Formulário de cadastro
├── dashboard_aluno.html       # Interface do aluno
├── dashboard_professor.html   # Interface do professor
├── formulario.html            # Nova solicitação
└── avaliar_solicitacao.html   # Avaliação (professor)
```

### Models (Backend):
```python
# Relacionamentos:
User (Django) ↔ Perfil (OneToOne)
User ↔ Solicitacao (ForeignKey - aluno)
User ↔ Solicitacao (ForeignKey - professor_responsavel)
Disciplina ↔ Solicitacao (ForeignKey)
```

### Media Files:
```
media/
└── solicitacoes/
    ├── 2025/
    │   ├── 01/          # Janeiro 2025
    │   ├── 02/          # Fevereiro 2025
    │   └── ...
    └── 2024/
        └── ...
```

## 🔮 Possíveis Melhorias Futuras

### Funcionalidades:
- [ ] **Notificações por email** quando status muda
- [ ] **Dashboard administrativo** para coordenadores
- [ ] **Relatórios e estatísticas** de solicitações
- [ ] **API REST** para integração com outros sistemas
- [ ] **Upload múltiplo** de arquivos
- [ ] **Comentários** entre aluno e professor
- [ ] **Histórico de alterações** de cada solicitação
- [ ] **Sistema de aprovação** em múltiplas etapas

### Técnicas:
- [ ] **Banco PostgreSQL** para produção
- [ ] **Redis** para cache e sessões
- [ ] **Celery** para processamento assíncrono
- [ ] **Docker** para containerização
- [ ] **Nginx** para servir arquivos estáticos
- [ ] **HTTPS** e certificados SSL
- [ ] **Backup automatizado** do banco
- [ ] **Testes automatizados** (unittest/pytest)

## 📊 Métricas do Projeto

- **Linhas de código Python**: ~400 linhas
- **Templates HTML**: 6 arquivos
- **Modelos de dados**: 3 classes
- **Views implementadas**: 7 funções
- **URLs configuradas**: 8 rotas
- **Disciplinas pré-cadastradas**: 20 itens
- **Campos de formulário**: 15+ campos
- **Funcionalidades JavaScript**: Busca dinâmica, filtros

## 🤝 Contribuição

Este projeto foi desenvolvido como sistema educacional e pode ser expandido conforme necessidade. Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é open source e está disponível sob a licença MIT.

---

**Desenvolvido com 💙 usando Django + TailwindCSS**

*Sistema completo e funcional para gerenciamento de solicitações de segunda chamada em instituições de ensino.*

## Fluxo de aprovação (Coordenação → Secretaria → Professor)
- Três etapas sequenciais: coordenação aprova primeiro, depois secretaria, depois professor.
- Justificativa obrigatória para coordenação ou qualquer rejeição.
- Prazo configurado por solicitação; se expirar sem conclusão, o pedido é rejeitado automaticamente.
- Aluno recebe notificação interna em cada decisão e ao expirar o prazo.
- Dashboards mostram fila por papel e histórico das avaliações feitas.
