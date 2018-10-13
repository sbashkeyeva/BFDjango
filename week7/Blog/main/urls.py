from django.urls import path
from . import views
urlpatterns =[
    path('', views.posts,name='posts'),
    path('home/', views.home, name='home'),
    path('add/',views.add, name='add'),
    path('detaile/<int:post_id>',views.detailed,name='detailed'),
    path('delete_all/',views.delete_all,name='delete_all')
]