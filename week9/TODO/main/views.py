from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.http import Http404


def home(request):
    return render(request, 'home.html')


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo_list.html', context)


def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
        context = {'form': form}
        return render(request, 'add_task.html', context)


def delete_task(request, id):
    task = Todo.objects.get(pk=id)
    task.delete()
    return redirect('todo_list')


def delete_all(request):
    task = Todo.objects.all()
    task.delete()
    return redirect('todo_list')


def completed(request):
    tasks=Todo.objects.filter(mark=True)
    context={'tasks':tasks}
    return render(request, 'completed_todo_list.html', context)

def detailed(request,id):
    try:
        task=Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        raise Http404('Not Found')
    context={'task':task}
    return render(request, 'detailed_task.html', context)


