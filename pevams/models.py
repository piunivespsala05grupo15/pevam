from django.db import models

class Cadastro(models.Model):
    numero_registro = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    lotacao = models.CharField(max_length=100)
    tipo_sanguineo = models.CharField(max_length=3)
    plano_saude = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class ContatoEmergencia(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)  # Relaciona com o modelo Cadastro
    nome_contato = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_contato
    
class EventoCritico(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('acidente', 'Acidente'),
        ('incendio', 'Incêndio'),
        ('emergencia_medica', 'Emergência Médica'),
    ]

    tipo_evento = models.CharField(max_length=50, choices=TIPO_EVENTO_CHOICES)

    def __str__(self):
        return self.tipo_evento
    
class Lotacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome