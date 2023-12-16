from django.urls import path

from portfolio import views

app_name = "portfolio"
urlpatterns = [
    path('', views.index, name='index'),
]