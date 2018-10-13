from django.urls import path, re_path
from . import views
urlpatterns =[
    path('home/', views.home, name='home'),

    re_path(r'^posts/read_post/(\d+)/', views.post_detailed, name='post_detailed'),
    path('todos/delete_all/', views.delete_all_posts, name='delete_all'),

    path('posts/', views.posts, name='posts'),
    path('posts/new_post/', views.add_post, name='add_post'),
    path('todos/delete_all/', views.delete_all_posts, name='delete_all'),
    re_path(r'^posts/update/(\d+)/', views.update_post, name='update_post'),

    re_path(r'^posts/delete_post/(\d+)/', views.delete_post, name='delete_post'),
    re_path(r'^todos/create_comment/(\d+)/', views.add_comment, name='add_comment'),

]