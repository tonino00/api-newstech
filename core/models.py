from django.db import models
from eventos.models import Evento
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class Noticia(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    eventos = models.ManyToManyField(Evento)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='noticias', null=True, blank=True)

    def __str__(self):
        return self.nome
