from django.db import models

# Create your models here.
class BlogPost(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    conteudo = models.TextField(verbose_name="Conteúdo")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    data_criada = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    imagem = models.ImageField(upload_to='blog_images/%Y/%m/%d/', verbose_name="Imagem")

class Autor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    bio = models.TextField(verbose_name="Biografia")
    profile_picture = models.ImageField(upload_to='autor_imagens/', verbose_name="Foto de Perfil")

