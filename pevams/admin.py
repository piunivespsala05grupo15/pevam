from django.contrib import admin
from .models import Cadastro, ContatoEmergencia, EventoCritico, Lotacao

admin.site.register(Cadastro)
admin.site.register(ContatoEmergencia)
admin.site.register(EventoCritico)
admin.site.register(Lotacao)
