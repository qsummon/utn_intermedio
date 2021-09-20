# from django.conf.urls import url
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )
from . import views

# Creacion de patterns con primary key para post/update/delete
urlpatterns = [
    # url('', views.home, name='lab-home'),
    path('', PostListView.as_view(), name='lab-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='lab-about'),
]
