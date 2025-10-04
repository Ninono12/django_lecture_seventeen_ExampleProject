from django.urls import path

from blog.views import create_blog_post, blog_post_list_create, BlogPostListCreateView, BlogPostDetailUpdateDeleteView

urlpatterns = [
    path('blog_create/', create_blog_post, name='create_blog_post'),
    path('blog_post_list_create/', blog_post_list_create, name='blog_post_list_create'),
    path('blog_post_list_create_class/', BlogPostListCreateView.as_view(), name='blog_post_list_create_class'),
    path('blogposts/<int:id>/', BlogPostDetailUpdateDeleteView.as_view(), name='blogposts_detail'),
]
