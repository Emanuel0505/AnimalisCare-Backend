from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class SiteConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.Charfied(max_lenght=255)
    descricao = models.TextField()
    urlBase = models.URLField()

    linkPrimario = models.Foreignkey(
        'CanalDeComunicacao',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class CanalDeComunicacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.Charfield(
        max_lenght=20,
        choices=CanalTipo.choices,
        default=CanalTipo.WHATSAPP,
    )
    label = models.CharField(max_lenght=100)
    url = models.URLField()
    ativo = models.BooleanField(default=True)

    site_config = models.Foreignkey(
        SiteConfig,
        on_delete=models.CASCADE,
        related_name='canais'
    )