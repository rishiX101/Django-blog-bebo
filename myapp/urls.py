from django.urls import path
from . import views
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user_posts'),
    path('posts/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create')
    # path('post/new/', views.create_post, name='post-create'),
]

