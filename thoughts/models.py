from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    """
    Database model for tags, to be attached
    to user-submitted thoughts
    """
    name = models.CharField(max_length=40)
    text_color = models.CharField(max_length=7)
    bg_color = models.CharField(max_length=7)

    # Shows tag colors in admin menu
    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: {}; background-color: {}">{}</span>',
            self.text_color,
            self.bg_color,
            self.name,
        )

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']


class Thought(models.Model):
    """
    Database model for user-submitted thoughts
    """
    title = models.CharField(
        max_length=96, null=False, blank=False, default="Untitled Thought")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='thoughts'
        )
    content = models.TextField(max_length=400, null=False, blank=False)
    time = models.TimeField(default=timezone.now)
    anonymous = models.BooleanField(null=False, blank=False, default=True)
    # auto_now_add applies only on creation while auto_now applies on update
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User,
        related_name="thought_likes",
        blank=True
        )
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-date_created']

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comment_thought.count()

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """
    Database model for comments, to be attached to thoughts
    """
    thought = models.ForeignKey(
        Thought,
        on_delete=models.CASCADE,
        related_name="comment_thought"
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_author'
        )
    content = models.TextField(max_length=280, null=False, blank=False)
    anonymous = models.BooleanField(null=False, blank=False, default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User,
        related_name="comment_likes",
        blank=True
        )

    class Meta:
        ordering = ['date_created']

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.author.get_short_name() + ": " + self.content)
