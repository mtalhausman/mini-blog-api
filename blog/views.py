from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .queries import get_top_3_posts, get_most_active_user


# ─── Post APIs ───────────────────────────────────────────

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments')).order_by('-created_at')


class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments'))


# ─── Comment APIs ────────────────────────────────────────

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['post_id']
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_id'])


# ─── Custom Endpoints ────────────────────────────────────

class Top3PostsView(APIView):
    """
    Returns top 3 posts with the highest number of comments.
    """
    def get(self, request):
        posts = list(get_top_3_posts())
        return Response(posts)


class MostActiveUserView(APIView):
    """
    Returns the most active user based on total comment count.
    """
    def get(self, request):
        user = get_most_active_user()
        if not user:
            return Response({'detail': 'No users found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'name': user.name,
            'email': user.email,
            'total_comments': user.total_comments
        })