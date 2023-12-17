from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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

def article(request, slug):
    context = {
        'profile': profile(1),
        'article': Article.objects.get(slug=slug)
    }
    return render(request, 'blog/article.html', context)