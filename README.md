# Sistema de Solicitação de Segunda Chamada

Este é um sistema Django desenvolvido no modelo MVT (Model-View-Template) para gerenciar solicitações de segunda chamada em ambientes acadêmicos.

## Funcionalidades

### Para Alunos:
- Registro e login no sistema
- Envio de solicitações de segunda chamada com motivo detalhado
- Visualização do status das solicitações (pendente, aprovada, rejeitada)
- Visualização de observações dos professores

### Para Professores:
- Login no sistema
- Visualização de todas as solicitações pendentes
- Aprovação ou rejeição de solicitações
- Adição de observações às decisões
- Histórico de avaliações realizadas

## Tecnologias Utilizadas

- **Django**: Framework web Python
- **HTML5**: Estrutura das páginas
- **CSS3**: Estilização responsiva
- **JavaScript**: Interações do lado cliente
- **SQLite**: Banco de dados (padrão Django)

## Estrutura do Projeto

```
segunda_chamada/
├── manage.py
├── segunda_chamada/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── solicitacoes/
    ├── models.py          # Modelos Perfil e Solicitacao
    ├── views.py           # Lógica das views
    ├── urls.py            # Rotas do app
    ├── admin.py
    ├── templates/solicitacoes/
    │   ├── login.html
    │   ├── registro.html
    │   ├── dashboard_aluno.html
    │   ├── dashboard_professor.html
    │   ├── formulario.html
    │   └── avaliar_solicitacao.html
    └── static/solicitacoes/
        ├── css/style.css  # Estilos responsivos
        └── js/main.js     # Scripts JavaScript
```

## Como usar

1. **Primeiro acesso**: Acesse `/registro/` para criar uma conta
2. **Login**: Faça login em `/` (página inicial)
3. **Alunos**: Serão redirecionados para o dashboard onde podem fazer novas solicitações
4. **Professores**: Serão redirecionados para o dashboard onde podem avaliar solicitações

## Instalação

1. Ative o ambiente virtual: `C:/repos/2Chamada/.venv/Scripts/python.exe`
2. Execute as migrations: `python manage.py migrate`
3. Inicie o servidor: `python manage.py runserver`
4. Acesse: http://127.0.0.1:8000

## Modelos de Dados

- **Perfil**: Estende o User do Django com tipo (aluno/professor) e matrícula
- **Solicitacao**: Armazena disciplina, motivo, status, datas e observações

O sistema está pronto para uso com interface profissional e funcionalidades completas!