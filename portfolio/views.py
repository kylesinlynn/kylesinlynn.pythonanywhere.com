from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Kyle Sin Lynn',
        'description': 'Kyle Sin Lynn, a dedicated software engineer, excels in Python and Django. Committed to innovation, problem-solving, and collaborative success.',
        'keywords': [
            'kylesinlynn',
            'Kyle Sin Lynn'
        ],
        'image': 'https://avatars.githubusercontent.com/u/82741688?v=4',
        'email': 'kylesinlynn@gmail.com',
        'phone': '+959766107203',
        'copyright': 2024,
        'facebook': 'danielhannaing',
        'x': 'kylesinlynn',
        'github': 'kylesinlynn',
        
        'works': [
                {
                    'client': 'Microsoft Inc',
                    'title': 'Management System',
                    'description': 'Better communication and control workflow on time',
                    'link': '#'
                },
                {
                    'client': 'Microsoft Inc',
                    'title': 'Management System',
                    'description': 'Better communication and control workflow on time',
                    'link': '#'
                },
                {
                    'client': 'Microsoft Inc',
                    'title': 'Management System',
                    'description': 'Better communication and control workflow on time',
                    'link': '#'
                },
                {
                    'client': 'Microsoft Inc',
                    'title': 'Management System',
                    'description': 'Better communication and control workflow on time',
                    'link': '#'
                },
            ],
    }
    return render(request, 'portfolio/index.html', context)