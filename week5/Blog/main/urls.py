
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts),
    path('posts/comments/', views.comments)
  ]