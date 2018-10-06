from django.shortcuts import render, redirect
from .models import User,Post,Comment
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def posts(request):
    posts = Post.objects.all()
    context = {
        'Post': posts
    }
    return render(request, 'posts.html', context)


@csrf_exempt
def comments(request):
    posts = Comment.objects.all()
    context = {
        'Comment': posts.comments.all()
    }
    return render(request, 'comments.html', context)

