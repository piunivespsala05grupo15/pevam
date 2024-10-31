from django.db import models

class Policial(models.Model):
    TIPO_SANGUE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    numero_registro = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    lotacao = models.CharField(max_length=100)
    tipo_sanguineo = models.CharField(max_length=50, choices=TIPO_SANGUE_CHOICES)
    plano_saude = models.CharField(max_length=100)
    numero_plasau = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class ContatoEmergencia(models.Model):
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    nome_contato = models.CharField(max_length=100)
    celular_contato = models.CharField(max_length=15)
    email_contato = models.CharField(max_length=50)


    def __str__(self):
        return self.nome_contato
    
class Local(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.logradouro
    
class Hospital(models.Model):
    nome = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    telefone = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

