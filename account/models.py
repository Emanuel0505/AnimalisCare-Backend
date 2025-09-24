import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomeCompleto = models.CharField(max_length=255, verbose_name="Nome Completo")
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografia")
    cargo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")
    fotoPerfil = models.ImageField(upload_to='foto_perfil/', verbose_name="Avatar")

    def __str__(self):
        return self.username