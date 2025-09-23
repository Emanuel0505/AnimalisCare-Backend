from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nomeCompleto = models.CharField(max_length=255, verbose_name="Nome Completo")
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografia")
    cargo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")
    fotoPerfil = models.ImageField(upload_to='foto_perfil/', verbose_name="Avatar")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username