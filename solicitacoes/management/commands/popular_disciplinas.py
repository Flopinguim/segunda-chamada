from django.core.management.base import BaseCommand
from solicitacoes.models import Disciplina

class Command(BaseCommand):
    help = 'Popula o banco com disciplinas de TI'
    
    def handle(self, *args, **options):
        disciplinas = [
            {'codigo': 'ALG001', 'nome': 'Algoritmos e Estruturas de Dados I', 'descricao': 'Introdução a algoritmos e estruturas de dados básicas'},
            {'codigo': 'ALG002', 'nome': 'Algoritmos e Estruturas de Dados II', 'descricao': 'Estruturas de dados avançadas e algoritmos de ordenação'},
            {'codigo': 'WEB001', 'nome': 'Desenvolvimento Web I', 'descricao': 'HTML, CSS, JavaScript básico'},
            {'codigo': 'WEB002', 'nome': 'Desenvolvimento Web II', 'descricao': 'Frameworks frontend e backend'},
            {'codigo': 'BD001', 'nome': 'Banco de Dados I', 'descricao': 'Modelagem e SQL básico'},
            {'codigo': 'BD002', 'nome': 'Banco de Dados II', 'descricao': 'Administração e otimização de bancos de dados'},
            {'codigo': 'JAVA001', 'nome': 'Programação Java I', 'descricao': 'Fundamentos da linguagem Java'},
            {'codigo': 'JAVA002', 'nome': 'Programação Java II', 'descricao': 'Java avançado e frameworks'},
            {'codigo': 'PY001', 'nome': 'Python para Iniciantes', 'descricao': 'Introdução à programação com Python'},
            {'codigo': 'PY002', 'nome': 'Python Avançado', 'descricao': 'Programação avançada em Python'},
            {'codigo': 'SO001', 'nome': 'Sistemas Operacionais', 'descricao': 'Conceitos de sistemas operacionais'},
            {'codigo': 'REDE001', 'nome': 'Redes de Computadores', 'descricao': 'Fundamentos de redes e protocolos'},
            {'codigo': 'SEC001', 'nome': 'Segurança da Informação', 'descricao': 'Princípios de segurança cibernética'},
            {'codigo': 'MOBILE001', 'nome': 'Desenvolvimento Mobile', 'descricao': 'Criação de aplicativos móveis'},
            {'codigo': 'IA001', 'nome': 'Inteligência Artificial', 'descricao': 'Introdução à IA e machine learning'},
            {'codigo': 'DEVOPS001', 'nome': 'DevOps e Cloud', 'descricao': 'Práticas DevOps e computação em nuvem'},
            {'codigo': 'PROJ001', 'nome': 'Gerenciamento de Projetos', 'descricao': 'Metodologias ágeis e gestão de projetos'},
            {'codigo': 'UX001', 'nome': 'UX/UI Design', 'descricao': 'Design de experiência do usuário'},
            {'codigo': 'TEST001', 'nome': 'Testes de Software', 'descricao': 'Técnicas de teste e qualidade de software'},
            {'codigo': 'API001', 'nome': 'Desenvolvimento de APIs', 'descricao': 'REST, GraphQL e microserviços'},
        ]
        
        for disc_data in disciplinas:
            disciplina, created = Disciplina.objects.get_or_create(
                codigo=disc_data['codigo'],
                defaults={
                    'nome': disc_data['nome'],
                    'descricao': disc_data['descricao'],
                    'ativo': True
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Disciplina criada: {disciplina.codigo} - {disciplina.nome}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Disciplina já existe: {disciplina.codigo}')
                )
        
        self.stdout.write(self.style.SUCCESS('Comando executado com sucesso!'))