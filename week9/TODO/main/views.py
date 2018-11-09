from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class TodoListView(ListView):
    template_name = 'todo_list.html'
    model = Todo
    context_object_name = 'todos'
    # def get_queryset(self):
    #     context = {}
    #     context['todos'] = Todo.objects.all()
    #     print (context['todos'])
    #     return context
    #
    # def get_context_data(self, **kwargs):
    #     context = super(TodoListView, self).get_context_data(**kwargs)
    #     context['todos'] = Todo.objects.all()
    #     return context


class TodoCreateView(CreateView):
    template_name = 'todo_form.html'
    model = Todo
    fields = ['name', 'created', 'dueon', 'owner', 'mark']
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        return Todo.objects.for_user(user=self.request.user)


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detailed_task.html'
    context_object_name = 'task'


class TodoUpdateView(UpdateView):
    model = Todo
    pk_url_kwarg = 'todo_pk'
    fields = ['name', 'created', 'dueon', 'owner', 'mark']
    template_name = 'todo_form.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        return Todo.objects.for_user(user=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # def form_valid(self,form):
    #     todo=form.save(commit=False)
    #     todo.updated_by=self.request.user
    #     todo.updated_at=timezone.now()
    #     todo.save()
    #     return redirect('topic_todo',pk=todo.topic.board.pk,topic_pk=todo.topic.pk)


class CompleteListView(ListView):
    model = Todo
    template_name = 'completed_todo_list.html'
    context_object_name = 'tasks'
    queryset = Todo.completed_object.all()


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
        return render(request, 'todo_form.html', context)


def delete_task(request, id):
    task = Todo.objects.get(pk=id)
    task.delete()
    return redirect('todo_list')


def delete_all(request):
    task = Todo.objects.all()
    task.delete()
    return redirect('todo_list')


def completed(request):
    tasks = Todo.objects.filter(mark=True)
    context = {'tasks': tasks}
    return render(request, 'completed_todo_list.html', context)


def detailed(request, id):
    try:
        task = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        raise Http404('Not Found')
    context = {'task': task}
    return render(request, 'detailed_task.html', context)
