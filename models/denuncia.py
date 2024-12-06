from django.db import models
from .empresa import Empresa
from django.contrib.auth.models import User

class Denuncia(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Análise', 'Em Análise'),
        ('Resolvida', 'Resolvida'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='denuncias')
    data_incidente = models.DateField()
    denunciante = models.CharField(max_length=100, default="Anônimo", blank=True, null=True)
    anexo = models.FileField(upload_to='denuncias/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='denuncias')  # Relaciona com o usuário

    def __str__(self):
        return self.titulo