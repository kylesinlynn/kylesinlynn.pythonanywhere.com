from django.core.paginator import Paginator
from django.shortcuts import render

from portfolio.models import Profile
from blog.models import Article

profile = lambda _: Profile.objects.latest('id')

def index(request):
    articles = Article.objects.all()
    page = request.GET.get("page") if 'page' in request.GET else 1
    
    paginator = Paginator(articles, 7)
    blog = paginator.get_page(page)
    
    context = {
        'profile': profile(7),
        'blog': blog
    }
    return render(request, 'blog/index.html', context)

def create(request):
    pass

def article(request, slug):
    context = {
        'profile': profile(1),
        'article': Article.objects.get(slug=slug)
    }
    return render(request, 'blog/article.html', context)