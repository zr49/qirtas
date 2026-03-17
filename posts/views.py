from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.db import models

def home_view(request):
    query = request.GET.get('q')
    published_posts = Post.objects.filter(status='published')
    if query:
        posts = published_posts.filter(
            models.Q(title__icontains=query) | models.Q(content__icontains=query)
        ).distinct()
    else:
        posts = published_posts.order_by('-date_created')
    return render(request, 'index.html', {'posts': posts, 'query': query})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {
            'post': post,
            'comments': comments,
            'form': form,
    })