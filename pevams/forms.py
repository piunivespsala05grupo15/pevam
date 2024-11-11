from django import forms
from .models import Policial, ContatoEmergencia, Hospital
from django.forms import inlineformset_factory

class PolicialForm(forms.ModelForm):
    class Meta:
        model = Policial
        fields = ['numero_registro', 'nome', 'lotacao', 'tipo_sanguineo', 'plano_saude', 'numero_plasau']
        widgets = {
            'numero_registro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10.001'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'João da Silva'}),
            'lotacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DELEGACIA DE CAMPINAS'}),
            'tipo_sanguineo': forms.Select(attrs={'class': 'form-select'}),
            'plano_saude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UNIMED'}),
            'numero_plasau': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000000000'}),
        }

ContatoEmergenciaFormSet = inlineformset_factory(
    Policial, ContatoEmergencia, form=forms.ModelForm, fields=['nome_contato', 'celular_contato', 'email_contato'],
    extra=1, can_delete=True
)

class ContatoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContatoEmergencia
        fields = ['nome_contato', 'celular_contato', 'email_contato']
        widgets = {
            'nome_contato': forms.TextInput(attrs={'placeholder': 'Nome do Contato', 'class': 'form-control'}),
            'celular_contato': forms.TextInput(attrs={'placeholder': 'Celular do Contato', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email do Contato', 'class': 'form-control'}),
        }


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'cep', 'latitude', 'longitude', 'telefone', 'forma_entrada']