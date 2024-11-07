# Generated by Django 5.1.1 on 2024-10-31 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pevams', '0006_contatoemergencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=15)),
                ('bairro', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=10)),
                ('cep', models.IntegerField(max_length=8)),
                ('latitude', models.IntegerField(max_length=20)),
                ('longitude', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='contatoemergencia',
            old_name='email',
            new_name='email_contato',
        ),
        migrations.AlterField(
            model_name='contatoemergencia',
            name='celular_contato',
            field=models.IntegerField(max_length=15),
        ),
    ]