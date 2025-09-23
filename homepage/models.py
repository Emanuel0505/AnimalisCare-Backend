from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class serviços(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Localizacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class Planos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    urlBase = models.URLField()
    contato = models.ManyToManyField('CanalDeComunicacao', blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço em R$")
    beneficios = models.TextField()

class Vantagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.ImageField(upload_to='icones/', blank=True, null=True)

class CanalDeComunicacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NomeCanal = models.CharField(max_length=50, verbose_name="Tipo de Canal")
    url = models.URLField()
    ativo = models.BooleanField(default=True)

class Contato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)

