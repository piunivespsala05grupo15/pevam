from django.contrib import admin
from .models import Policial, ContatoEmergencia, Local, Hospital, User

admin.site.register(Policial)
admin.site.register(ContatoEmergencia)
admin.site.register(Local)
admin.site.register(Hospital)
admin.site.register(User)

