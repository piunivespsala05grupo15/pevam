# Generated by Django 5.1.1 on 2024-10-30 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pevams', '0005_policial_remove_contatoemergencia_cadastro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoEmergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=100)),
                ('celular_contato', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('policial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pevams.policial')),
            ],
        ),
    ]
