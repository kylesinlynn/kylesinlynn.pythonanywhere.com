from django.shortcuts import render

from portfolio.models import Profile
from blog.models import Article

profile = lambda _: Profile.objects.latest('id')

def index(request):
    context = {
        'profile': profile(1),
        'blog': Article.objects.all()
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