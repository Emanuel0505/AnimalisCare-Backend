from django.shortcuts import render,  redirect, get_object_or_404
from django.db.models import Count, Q, F
from django.urls import reverse
from .models import BlogPost, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from homepage.models import Contato


def blog_home(request):
    blog_post = BlogPost.objects.all().prefetch_related('tags')
    blog_bar = BlogPost.objects.all().prefetch_related('tags')

    #contatos
    contato = Contato.objects.all()


    # Filtragem por múltiplas tags (todas devem estar presentes)
    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        blog_post = (
            BlogPost.objects.filter(tags__nome__in=selected_tags)
            .annotate(num_tags=Count("tags", filter=Q(tags__nome__in=selected_tags), distinct=True))
            .filter(num_tags=len(selected_tags))
        )

    # ordenação do blog_bar (mais popular) e pequena paginação
    blog_bar = blog_bar.order_by('-views')[:10]

    # Ordenação(mais recente, mais antigo, e mais popular)

    ordem = request.GET.get('ordem')
    if ordem == 'recente':
        blog_post = blog_post.order_by('-data_criada')
    elif ordem == 'antigo':
        blog_post = blog_post.order_by('data_criada')
    elif ordem == 'popular':
        blog_post = blog_post.order_by('-views')

    # Paginação
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_post, 6)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'blog_post': result,
        'blog_bar': blog_bar,
        'all_tags': Tag.objects.all(),
        'selected_tags': selected_tags,
        'contato': contato,
    }

    return render(request, 'blog-page.html', context)


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

def view_detalhe(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id);
    views_posts = request.session.get('views_posts', [])

    if blog_id not in views_posts:
        BlogPost.objects.filter(id=blog_post.id).update(views=F('views') + 1)
        blog_post.refresh_from_db()

        views_posts.append(blog_id)
        request.session['views_posts'] = views_posts

    next_url = request.GET.get('next') or reverse('blog')
    return redirect(next_url)