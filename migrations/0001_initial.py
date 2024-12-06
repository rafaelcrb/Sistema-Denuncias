# Generated by Django 5.1.3 on 2024-11-15 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data_incidente', models.DateField()),
                ('denunciante', models.CharField(blank=True, default='Anônimo', max_length=100, null=True)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='denuncias/')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Em Análise', 'Em Análise'), ('Resolvida', 'Resolvida')], default='Pendente', max_length=20)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denuncias', to='denuncias.empresa')),
            ],
        ),
    ]
