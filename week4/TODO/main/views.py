from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Todo,Human

from django.http import HttpResponse

def listed(request):
    todo_list=Todo.objects.order_by('id')

    context={'todo_list': todo_list}
    return render(request,'todo_list.html',context)

def completed(request):
    completed_todo_list = Todo.objects.filter(mark=True)

    context = {'keys': completed_todo_list}
    return render(request,'completed_todo_list.html',context)
