from django.contrib import admin
from .models import Policial, ContatoEmergencia, Local, Hospital

admin.site.register(Policial)
admin.site.register(ContatoEmergencia)
admin.site.register(Local)
admin.site.register(Hospital)

