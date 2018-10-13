from django.db import models
from django.forms import ModelForm
from .models import Posts, Comment


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = {'title', 'author', 'content', 'date'}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'date', 'comment'}