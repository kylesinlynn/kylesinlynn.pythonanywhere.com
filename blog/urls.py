from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('article/', views.create, name="create"),
    path('article/<slug>', views.article, name="article"),
    path('article/<slug>/update', views.update, name="update"),
]