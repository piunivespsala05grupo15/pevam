from django import forms
from .models import Policial, ContatoEmergencia

class PolicialForm(forms.ModelForm):
    class Meta:
        model = Policial
        fields = ['numero_registro', 'nome', 'lotacao', 'tipo_sanguineo', 'plano_saude', 'numero_plasau']

        widgets = {
            'numero_registro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10.001',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'João da Silva',
            }),
            'lotacao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'DELEGACIA DE CAMPINAS',
            }),
            'tipo_sanguineo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A+',
            }),
            'plano_saude': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UNIMED',
            }),
            'numero_plasau': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000000000',
            }),
        }

class ContatoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContatoEmergencia
        fields = ['nome_contato', 'celular_contato', 'email_contato']
        widgets = {
            'nome_contato': forms.TextInput(attrs={'placeholder': 'Nome do Contato', 'class': 'form-control'}),
            'celular_contato': forms.TextInput(attrs={'placeholder': 'Celular do Contato', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email do Contato', 'class': 'form-control'}),
        }