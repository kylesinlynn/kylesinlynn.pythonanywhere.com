from django.core.paginator import Paginator
from django.shortcuts import render

from portfolio.models import Profile
from blog.models import Article

profile = lambda _: Profile.objects.latest('id')

def index(request):
    articles = Article.objects.all()
    page = request.GET.get("page") if 'page' in request.GET else 1
    
    paginator = Paginator(articles, 1)
    blog = paginator.get_page(page)
    
    context = {
        'profile': profile(1),
        'blog': blog
    }
    return render(request, 'blog/index.html', context)

def create(request):
    pass

def article(request, id):
    context = {
        'profile': profile(1),
        'article': Article.objects.get(pk=id)
    }
    return render(request, 'blog/article.html', context)