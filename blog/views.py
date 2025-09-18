from django.shortcuts import render, redirect
from .models import BlogPost


def blog_home(request):
    blog_post = BlogPost.objects.all()

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'index.html', context)


def create_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        autor = request.POST.get('autor')
        imagem = request.FILES.get('imagem')
        
        blog_post = BlogPost(
            titulo=titulo,
            conteudo=conteudo,
            autor=autor,
            imagem=imagem
        )

        blog_post.save()

    return render(request, 'blog_create.html')
