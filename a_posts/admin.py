from django.contrib import admin

from .models import Post, Tag, Comment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['tags']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = (
        ('Tag', {
            'fields': ('name', 'image')
        }),
    )

admin.site.register(Comment)
admin.site.register(Reply)
