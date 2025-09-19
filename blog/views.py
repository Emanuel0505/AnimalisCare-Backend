from django.shortcuts import render, redirect
from .models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_home(request):
    blog_post = BlogPost.objects.all()

    pagina = request.GET.get('pagina', 1)
    paginator = Paginator(blog_post, 6)

    try:
        result = paginator.page(pagina)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'blog_post': result,
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
