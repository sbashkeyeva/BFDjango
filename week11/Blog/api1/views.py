from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from main.models import Post, Comment


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts = [p.to_json() for p in posts]
        return JsonResponse(posts, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        post = Post(
            title=data['title'],
            content=data['content'],
            date=data['date'],
            #created_by=data['created_by'],
        )
        post.save()
        return JsonResponse(post.to_json())


@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(post.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        post.title = data.get['title']
        post.content = data.get['content']
        post.date = data.get['date']
        post.save()
        return JsonResponse(post.to_json())
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True}, status=204)


@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        comments = [c.to_json() for c in comments]
        return JsonResponse(comments, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        post = Post(content=data['content'], date=data['date'])
        post.save()
        return JsonResponse(post.to_json())


@csrf_exempt
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)
    if request.method == 'GET':
        return JsonResponse(comment.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        comment.content = data.get['content']
        comment.date = data.get['date']
    elif request.method == 'DELETE':
        comment.delete()
        return JsonResponse({'deleted': True}, status=204)
