from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('todos/', views.todo_list, name='todo_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:id>/',views.delete_task, name='delete_task'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('comleted_todo_list/', views.completed, name='completed'),
    path('detailed_task/<int:id>/',views.detailed, name='detailed'),

]
