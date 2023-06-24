from django.contrib import admin
from .models import Thought, Comment, Tag


# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # Shows colors of tag in admin menu
    list_display = ('name', 'colored_name')


@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'author', 'time', 'date_updated', 'anonymous')
    list_filter = ('date_created', 'date_updated', 'anonymous')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['author', 'content']
    list_display = ('author', 'date_created', 'anonymous')
    list_filter = ('date_created', 'anonymous')
