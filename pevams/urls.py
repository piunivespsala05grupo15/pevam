from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policial/', views.policial, name='policial'),
    path('policial/<int:pk>/edit/', views.edit_policial, name='edit_policial'),
    path('policial/<int:pk>/delete/', views.delete_policial, name='delete_policial'),
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<int:pk>/edit/', views.edit_hospital, name='edit_hospital'),
    path('hospital/<int:pk>/delete/', views.delete_hospital, name='delete_hospital'),
    path('contato_emergencia/', views.contato_emergencia, name='contato_emergencia'),
    path('local/', views.local, name="local"),
    path('pevam/', views.criar_pevam, name='criar_pevam'),
    path('policial/list/', views.list_policial, name='list_policial'),
    path('hospital/list/', views.list_hospital, name='list_hospital'),
	
    path('cadastro_agente/', views.cadastro_agente, name='cadastro_agente'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]