from django.contrib import admin
from blog.models import BlogPost, BlogPostImage, Author, BannerImage

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'deleted')
    list_filter = ('deleted',)

admin.site.register(BlogPostImage)
admin.site.register(Author)
admin.site.register(BannerImage)