from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('todos/', views.TodoListView.as_view(), name='todo_list'),
    path('add_task/', views.TodoCreateView.as_view(), name='add_task'),
    path('delete_task/<int:pk>/',views.TodoDeleteView.as_view(), name='delete_task'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('comleted_todo_list/', views.CompleteListView.as_view(), name='completed'),
    path('detailed_task/<int:pk>/',views.TodoDetailView.as_view(), name='detailed'),
    path('update_task/<int:todo_pk>/',views.TodoUpdateView.as_view(),name='update_task')

]
