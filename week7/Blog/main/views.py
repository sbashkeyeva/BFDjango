from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

import datetime
from datetime import timedelta
from .models import Comment, Posts
from .forms import PostForm, CommentForm

def home(request):
    return render(request,'home.html')
def posts(request):
    post_list = Posts.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'posts.html', context)


def post_detailed(request, id):
    try:
        post = Posts.objects.get(pk=id)
    except Posts.DoesNotExist:
        raise Http404("Post was not found")
    context = {
        'posts': post
    }
    return render(request, 'post_detailed.html', context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm
    context ={
        'form': form
    }
    return render(request, 'add_post.html', context)

def update_post(request, id):
    updated_post = get_object_or_404(Posts, pk=id)
    form = PostForm(request.POST or None, instance=updated_post)
    if form.is_valid():
        form.save()
        return redirect(posts)
    return render(request, 'add_post.html', {'form': form})

def delete_post(request, id):
    deleted_post = Posts.objects.get(pk=id)
    deleted_post.delete()
    return redirect(posts)

def delete_all_posts(request):
    all_posts = Posts.objects.all()
    all_posts.delete()
    return redirect(posts)

def add_comment(request, id):
    post = get_object_or_404(Posts, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect('posts')
    else:
        form = CommentForm
    context = {
        'form': form
    }
    return render(request, 'add_comment.html', context)


