from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policial/', views.policial, name='policial'),
    path('contato_emergencia/', views.contato_emergencia, name='contato_emergencia'),
    path('local/', views.local, name="local"),
    path('hospital/', views.hospital, name="hospital"),
]