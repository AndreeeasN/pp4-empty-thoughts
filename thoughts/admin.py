from django.contrib import admin
from .models import Thought, Tag


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
