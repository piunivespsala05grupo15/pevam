from django import forms
from .models import Policial, ContatoEmergencia, Hospital
from django.forms import inlineformset_factory

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PolicialForm(forms.ModelForm):
    class Meta:
        model = Policial
        fields = ['numero_registro', 'nome', 'lotacao', 'tipo_sanguineo', 'plano_saude', 'numero_plasau']

class ContatoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContatoEmergencia
        fields = ['nome_contato', 'celular_contato', 'email_contato']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'cep', 'latitude', 'longitude', 'telefone', 'forma_entrada']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")