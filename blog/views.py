from django.shortcuts import render, redirect
from django.db.models import Count, Q
from .models import BlogPost, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_home(request):
    blog_post = BlogPost.objects.all().prefetch_related('tags')

    # Filtragem por múltiplas tags (todas devem estar presentes)
    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        blog_post = (
            BlogPost.objects.filter(tags__nome__in=selected_tags)
            .annotate(num_tags=Count("tags", filter=Q(tags__nome__in=selected_tags), distinct=True))
            .filter(num_tags=len(selected_tags))
        )


    # Paginação
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
        'all_tags': Tag.objects.all(),
        'selected_tags': selected_tags,
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

def create_tag(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        
        tag = Tag(
            nome=nome,
            descricao=descricao
        )

        tag.save()

    return render(request, 'blog_create.html')
