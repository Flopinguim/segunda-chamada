from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/aluno/', views.dashboard_aluno, name='dashboard_aluno'),
    path('dashboard/professor/', views.dashboard_professor, name='dashboard_professor'),
    path('nova-solicitacao/', views.nova_solicitacao, name='nova_solicitacao'),
    path('avaliar/<int:solicitacao_id>/', views.avaliar_solicitacao, name='avaliar_solicitacao'),
]
