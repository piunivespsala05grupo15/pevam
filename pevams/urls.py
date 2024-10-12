from django.urls import path
from . import views
from .views import CadastrarEventoCritico

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato_emergencia/', views.contato_emergencia, name='contato_emergencia'),
    path('cadastrar_evento_critico/', views.CadastrarEventoCritico.as_view(), name='cadastrar_evento_critico'),
    path('cadastrar_lotacao/', views.cadastrar_lotacao, name='cadastrar_lotacao'), 
]