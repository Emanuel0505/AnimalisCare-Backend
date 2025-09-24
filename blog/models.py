import uuid
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200, verbose_name="Título")
    conteudo = models.TextField(verbose_name="Conteúdo")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    data_criada = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    imagem = models.ImageField(upload_to='blog_images/%Y/%m/%d/')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    views = models.PositiveIntegerField(default=0, verbose_name="Número de Visualizações")


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome da Tag")
    descricao = models.TextField(verbose_name="Descrição da Tag")
    cor = models.CharField(max_length=7, verbose_name="Cor da Tag (Hex)", default="#FFFFFF")
    