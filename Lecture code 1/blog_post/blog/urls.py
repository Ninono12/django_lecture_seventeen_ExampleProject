from django.urls import path
from blog.views import (
    create_blog_post,
    BlogPostListCreateView,
    BlogPostDetailUpdateDeleteView,
    blog_post_list_detail_update,
)

urlpatterns = [
    path('blog_create/', create_blog_post, name='create_blog_post'),
    path('blog_post_list_create_class/', BlogPostListCreateView.as_view(), name='blog_post_list_create_class'),
    path('blogposts/<int:id>/', BlogPostDetailUpdateDeleteView.as_view(), name='blogposts_detail'),
    path('blog_post_detail_update/', blog_post_list_detail_update, name='blog_post_detail_update'),
]











