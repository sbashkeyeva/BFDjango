from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView
)


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'post_confirm_delete.html'


class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields = ['title', 'content']
    template_name = 'post_form.html'


class CommentUpdateView(UpdateView):
    model = Comment
    success_url = reverse_lazy('post_list')
    fields = ['content']
    template_name = 'comment_form.html'


class CommentCreateView(CreateView):
    model = Comment
    context_object_name = 'comments'
    fields = ['content']
    template_name = 'comment_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.post = post
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    success_url = reverse_lazy('post_list')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


class HomeView(TemplateView):
    template_name = 'home.html'


def home(request):
    return render(request, 'home.html')
