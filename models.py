from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

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

    def __str__(self):
        return self.titulo
