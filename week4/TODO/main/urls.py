from django.urls import path
from . import views
urlpatterns =[
    path('',views.listed),
    path('1/completed/',views.completed)
]