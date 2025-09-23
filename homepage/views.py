from django.shortcuts import render

from homepage.models import CanalDeComunicacao, Contato, Localizacao, Planos, serviços, Vantagem

# Create your views here.

def index(request):
    servicos = serviços.objects.all()
    planos = Planos.objects.all()
    vantagens = Vantagem.objects.all()
    canais = CanalDeComunicacao.objects.filter(ativo=True)
    localizacao = Localizacao.objects.all()
    contato = Contato.objects.all()


    context = {
        'servicos': servicos,
        'planos': planos,
        'vantagens': vantagens,
        'canais': canais,
        'localizacao': localizacao,
        'contato': contato,
    }

    return render(request, 'index.html', context)