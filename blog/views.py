from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def posts(request):
	posts = Post.objects.all().order_by('-created_date')
	return render(request, 'blog/posts.html',
		{
			'posts': posts,
		})

def post(request, id):
	post = get_object_or_404(Post, pk=id)
	return render(request, 'blog/post.html', 
		{
			'post': post,
		})