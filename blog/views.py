from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

''' Non-auth views'''
def posts(request):
	posts = Post.objects.all().order_by('-created_date')
	return render(request, 'blog/posts.html', {'posts': posts})

def post(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'blog/post.html', {'post': post})

''' Auth views '''
@login_required
def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish()
		return redirect('posts')
	else:
		form = PostForm()
		return render(request, 'blog/new_post.html', {'form': form})

@login_required
def edit_post(request, id):
	post = get_object_or_404(Post, id=id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.publish()
		return redirect('posts')
	else:
		form = PostForm(instance=post)
		return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, id):
	post = get_object_or_404(Post, id=id)
	post.delete()
	return redirect('posts')
