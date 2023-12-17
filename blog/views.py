from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render, get_object_or_404
from django.http import QueryDict

from portfolio.models import Profile
from blog.models import Article
from blog.forms import ArticleForm

profile = lambda _: Profile.objects.latest('id')

def index(request):
    articles = Article.objects.all()
    page = request.GET.get("page") if 'page' in request.GET else 1
    
    paginator = Paginator(articles, 7)
    blog = paginator.get_page(page)
    
    context = {
        'profile': profile(1),
        'blog': blog
    }
    return render(request, 'blog/index.html', context)

def article(request, slug):
    context = {
        'profile': profile(1),
        'article': get_object_or_404(Article, slug=slug)
    }
    return render(request, 'blog/article.html', context)

@login_required
def create(request):
    context = {
        'profile': profile(1),
        'form': ArticleForm()
    }
    if request.method == 'POST':
        context['form'] = ArticleForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            return redirect('blog:index')
    return render(request, 'blog/create.html', context)

@login_required
@require_http_methods(['GET', 'POST', 'DELETE'])
def update(request, slug):
    context = {
        'profile': profile(1),
        'article': get_object_or_404(Article, slug=slug),
        'form': ArticleForm()
    }
    match request.method:
        case 'POST':
            context['form'] = ArticleForm(request.POST, request.FILES, instance=context['article'])
            if context['form'].is_valid():
                article = context['form'].save()
                return redirect('blog:article', article.slug)
        case 'DELETE':
            Article.objects.get(slug=slug).delete()
            return redirect('blog:index')
    return render(request, 'blog/update.html', context)