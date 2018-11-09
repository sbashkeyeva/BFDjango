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


class PostListView(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'post_confirm_delete.html'

    def get_queryset(self):
        return Post.objects.for_user(self.request.user)


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def get_queryset(self):
        return Post.objects.for_user(self.request.user)


class CommentUpdateView(UpdateView, LoginRequiredMixin):
    model = Comment
    success_url = reverse_lazy('post_list')
    fields = ['content']
    template_name = 'comment_form.html'


class CommentCreateView(CreateView, LoginRequiredMixin):
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


class CommentDeleteView(DeleteView, LoginRequiredMixin):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    success_url = reverse_lazy('post_list')


class PostDetailView(DetailView, LoginRequiredMixin):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


class HomeView(TemplateView):
    template_name = 'home.html'


def home(request):
    return render(request, 'home.html')
