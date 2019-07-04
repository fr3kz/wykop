from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.Posts.as_view(), name="posts"),
    path('like_post/<int:post_id>',views.like_post, name="likepost"),
    path('dislike_post/<int:post_id>',views.dislike_post, name="dislikepost"),
    path('comments/<int:post_id>',views.Comments.as_view(), name="comments"),
    
]