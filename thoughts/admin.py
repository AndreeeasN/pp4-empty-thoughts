from django.contrib import admin
from .models import Thought, Comment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Displays tags and their colors in the admin menu
    """
    search_fields = ['name']
    list_display = ('name', 'colored_name')


@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    """
    Displays user-submitted thoughts in the admin menu
    """
    search_fields = ['title', 'content', 'author__username']
    list_display = ('title', 'author', 'time', 'date_updated', 'anonymous')
    list_filter = ('date_created', 'date_updated', 'anonymous')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Displays comments in the admin menu
    """
    search_fields = ['author__username', 'content']
    list_display = ('author', 'content', 'date_created', 'anonymous')
    list_filter = ('date_created', 'anonymous')
