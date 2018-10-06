from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Todo,Human
from .forms import TodoForm
from django.http import Http404

from django.http import HttpResponse

def listed(request):
    if request.method == 'POST':
        Todo.objects.all().delete()
        return redirect('jai')
    else:
        todo_list=Todo.objects.order_by('id')

        context={'todo_list': todo_list}
        return render(request,'todo_list.html',context)

def completed(request):
    completed_todo_list = Todo.objects.filter(mark=True)

    context = {'keys': completed_todo_list}
    return render(request,'completed_todo_list.html',context)

def add_task(request):
     print(request)
     if request.method=='POST':
         form=TodoForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('../')
         else:
             print('lalalala')
             return HttpResponse("aoaoao")
     else:
         form=TodoForm()
         context={
             'form': form
         }
         return render(request, 'add_task.html', context)


def detailed(request,task_id):
    if request.method=='POST':
        Todo.objects.filter(id=task_id).delete()
        return redirect('../')

    try:
        task=Todo.objects.get(id=task_id)
    except Todo.DoesNotExist:
        raise Http404('Not Found')

    context={
        'task': task
    }

    return render(request,'detailed.html',context)
