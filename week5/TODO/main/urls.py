from django.urls import path
from . import views

urlpatterns = [
    path('', views.listed, name='jai'),
    path('1/completed/',views.completed , name = "completed"),
    path('add/',views.add_task, name='add'),
    path('detail/<int:task_id>',views.detailed, name='detailed')


]