from django import forms
from .models import Cadastro, ContatoEmergencia, EventoCritico, Lotacao

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['numero_registro', 'nome', 'lotacao', 'tipo_sanguineo', 'plano_saude']

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
        }

class ContatoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContatoEmergencia
        fields = ['nome_contato', 'telefone_contato']
        widgets = {
            'nome_contato': forms.TextInput(attrs={'placeholder': 'Nome do Contato', 'class': 'form-control'}),
            'telefone_contato': forms.TextInput(attrs={'placeholder': 'Telefone do Contato', 'class': 'form-control'}),
        }

class EventoCriticoForm(forms.ModelForm):
    class Meta:
        model = EventoCritico
        fields = ['tipo_evento']

class LotacaoForm(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = ['nome']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DELEGACIA DE CAMPINAS'}),
        }