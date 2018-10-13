from django import forms
from .models import Comment, Post, User
from django.forms import ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','author','content','date')