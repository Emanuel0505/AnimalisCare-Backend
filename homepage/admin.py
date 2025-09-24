from django.contrib import admin
from .models import serviços, Localizacao, Planos, Vantagem, CanalDeComunicacao, Contato

# Register your models here.
admin.site.register(serviços)
admin.site.register(Localizacao)
admin.site.register(Planos)
admin.site.register(Vantagem)
admin.site.register(CanalDeComunicacao)
admin.site.register(Contato)