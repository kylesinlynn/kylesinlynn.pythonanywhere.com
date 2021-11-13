from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
	path('', views.posts, name='posts'),
	path('<int:id>/', views.post, name='post'),
	path('new_post/', views.new_post, name='new_post'),
	path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
	path('delete_post/<int:id>', views.delete_post, name='delete_post'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]