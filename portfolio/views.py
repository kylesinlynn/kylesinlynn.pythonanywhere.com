from django.shortcuts import render
from portfolio.models import Profile
# Create your views here.
def index(request):
    context = {
        'profile': Profile.objects.latest('id')
    }
    return render(request, 'portfolio/index.html', context)