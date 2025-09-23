from django.db import models

class Historia_valor(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    conteudo = models.TextField(verbose_name="Conteúdo")
    imagem = models.ImageField(upload_to='sobre_nos_images/%Y/%m/%d/', verbose_name="Imagem")
    valores = models.TextField(verbose_name="Valores")

class Equipe(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    descricao = models.TextField(verbose_name="Descrição")
    foto = models.ImageField(upload_to='equipe_fotos/', verbose_name="Foto")