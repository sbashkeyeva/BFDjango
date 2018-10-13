from django.shortcuts import render, redirect
from .models import Post,User, Comment
from django.http import Http404
from .forms import  PostForm

def posts(request):
    posts=Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'posts.html', context)

def comments(request):
    comments=Comment.objects.all()
    context={
        'comments': comments
    }

    return render(request,'commments.html', context)
def home(request):
    return render(request,'home.html')
def add(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form=PostForm

    context={
        'form' : form
    }

    return render(request,'add_posts.html',context)
def detailed(request, post_id):
    try:
        Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('Not Found')
    context={
        'posts':posts
    }

    return(request,'detailed.html', context)
def delete_all(request):
    posts=Post.objects.all()
    posts.delete()
    return redirect('posts')
