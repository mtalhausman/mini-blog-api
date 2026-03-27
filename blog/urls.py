from django.urls import path
from . import views

urlpatterns = [
    # Posts
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostRetrieveView.as_view(), name='post-retrieve'),

    # Comments
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),

    # Custom
    path('top-posts/', views.Top3PostsView.as_view(), name='top-posts'),
    path('most-active-user/', views.MostActiveUserView.as_view(), name='most-active-user'),
]