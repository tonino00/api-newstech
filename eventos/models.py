from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_event = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to='eventos', null=True, blank=True)

    def __str__(self):
        return self.nome
