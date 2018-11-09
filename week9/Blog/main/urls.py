from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.HomeView.as_view(), name='home'),
    path('post_list/',views.PostListView.as_view(),name='post_list'),
    path('add_post/',views.PostCreateView.as_view(), name='add_post'),
    path('delete_post/<int:pk>/',views.PostDeleteView.as_view(),name='delete_post'),
    path('detail_post/<int:pk>/',views.PostDetailView.as_view(),name='detail_post'),
    path('<int:pk>/add_comment/',views.CommentCreateView.as_view(),name='add_comment'),

]