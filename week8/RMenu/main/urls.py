from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('rests/',views.rests, name='rests'),
    path('detailed_rest/<int:id>/',views.detailed_rest, name='detailed_rest'),
    path('add_rest/', views.add_rest,name='add_rest'),
    path('delete_rest/<int:id>/', views.delete_rest, name='delete_rest'),
    path('update_rest/<int:id>/', views.update_rest, name='update_rest'),
    path('delete_all_rest/', views.delete_all_rest, name='delete_all_rest')

]