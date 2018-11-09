from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('rests/',views.RestListView.as_view(), name='rests'),
    path('detailed_rest/<int:pk>/',views.RestDetailView.as_view(), name='detailed_rest'),
    path('add_rest/', views.RestCreateView.as_view(),name='add_rest'),
    path('delete_rest/<int:pk>/', views.RestDeleteView.as_view(), name='delete_rest'),
    path('update_rest/<int:pk>/', views.RestUpdateView.as_view(), name='update_rest'),
    path('delete_all_rest/', views.delete_all_rest, name='delete_all_rest'),
    path('<int:id>/add_dish/', views.add_dish, name='add_dish'),


]