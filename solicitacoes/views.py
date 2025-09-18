from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Solicitacao, Perfil, Disciplina

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            try:
                perfil = user.perfil
                if perfil.tipo == 'professor':
                    return redirect('dashboard_professor')
                else:
                    return redirect('dashboard_aluno')
            except Perfil.DoesNotExist:
                return redirect('dashboard_aluno')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'solicitacoes/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        tipo = request.POST['tipo']
        matricula = request.POST.get('matricula', '')
        
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'solicitacoes/registro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'solicitacoes/registro.html')
        
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1
        )
        
        Perfil.objects.create(
            user=user,
            tipo=tipo,
            matricula=matricula if matricula else None
        )
        
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('login')
    
    return render(request, 'solicitacoes/registro.html')

@login_required
def dashboard_aluno(request):
    try:
        perfil = request.user.perfil
        if perfil.tipo != 'aluno':
            return redirect('dashboard_professor')
    except Perfil.DoesNotExist:
        pass
    
    solicitacoes = Solicitacao.objects.filter(aluno=request.user)
    return render(request, 'solicitacoes/dashboard_aluno.html', {
        'solicitacoes': solicitacoes
    })

@login_required
def dashboard_professor(request):
    try:
        perfil = request.user.perfil
        if perfil.tipo != 'professor':
            return redirect('dashboard_aluno')
    except Perfil.DoesNotExist:
        return redirect('dashboard_aluno')
    
    solicitacoes_pendentes = Solicitacao.objects.filter(status='pendente')
    solicitacoes_avaliadas = Solicitacao.objects.filter(professor_responsavel=request.user)
    disciplinas = Disciplina.objects.all().order_by('nome')
    
    return render(request, 'solicitacoes/dashboard_professor.html', {
        'solicitacoes_pendentes': solicitacoes_pendentes,
        'solicitacoes_avaliadas': solicitacoes_avaliadas,
        'disciplinas': disciplinas
    })

@login_required
def nova_solicitacao(request):
    try:
        perfil = request.user.perfil
        if perfil.tipo != 'aluno':
            return redirect('dashboard_professor')
    except Perfil.DoesNotExist:
        pass
    
    disciplinas = Disciplina.objects.filter(ativo=True)
    
    if request.method == 'POST':
        disciplina_id = request.POST.get('disciplina')
        motivo = request.POST.get('motivo')
        arquivo = request.FILES.get('arquivo')
        
        try:
            disciplina = Disciplina.objects.get(id=disciplina_id)
            solicitacao = Solicitacao.objects.create(
                aluno=request.user,
                disciplina=disciplina,
                motivo=motivo
            )
            
            if arquivo:
                solicitacao.arquivo = arquivo
                solicitacao.save()
            
            messages.success(request, 'Solicitação enviada com sucesso!')
            return redirect('dashboard_aluno')
        except Disciplina.DoesNotExist:
            messages.error(request, 'Disciplina inválida.')
    
    return render(request, 'solicitacoes/formulario.html', {
        'disciplinas': disciplinas
    })

@login_required
def avaliar_solicitacao(request, solicitacao_id):
    try:
        perfil = request.user.perfil
        if perfil.tipo != 'professor':
            return redirect('dashboard_aluno')
    except Perfil.DoesNotExist:
        return redirect('dashboard_aluno')
    
    solicitacao = get_object_or_404(Solicitacao, id=solicitacao_id, status='pendente')
    
    if request.method == 'POST':
        decisao = request.POST.get('decisao')
        observacoes = request.POST.get('observacoes', '')
        
        solicitacao.status = decisao
        solicitacao.professor_responsavel = request.user
        solicitacao.observacoes_professor = observacoes
        solicitacao.data_avaliacao = timezone.now()
        solicitacao.save()
        
        messages.success(request, f'Solicitação {decisao} com sucesso!')
        return redirect('dashboard_professor')
    
    return render(request, 'solicitacoes/avaliar_solicitacao.html', {
        'solicitacao': solicitacao
    })
