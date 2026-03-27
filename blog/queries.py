from django.db.models import Count
from .models import User, Post, Comment


# Query 1: Top 3 posts with highest number of comments
def get_top_3_posts():
    return Post.objects.annotate(
        comment_count=Count('comments')
    ).order_by('-comment_count')[:3].values('title', 'comment_count')


# Query 2: Users who have written more than 3 comments
def get_active_users():
    return User.objects.annotate(
        total_comments=Count('comments')
    ).filter(total_comments__gt=3).values('name', 'total_comments')


# Query 3: Most active user (highest number of comments)
def get_most_active_user():
    return User.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments').first()


# Query 4: All comments for a given post (newest first)
def get_comments_for_post(post_id):
    return Comment.objects.filter(
        post_id=post_id
    ).order_by('-created_at').values('user__name', 'comment_text', 'created_at')