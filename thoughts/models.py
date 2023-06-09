from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thought(models.Model):
    """
    Database model for user-submitted thoughts
    """
    title = models.CharField(max_length=48, null=False, blank=False, default="Untitled Thought")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280, null=False, blank=False)
    date = models.DateTimeField()
    anonymous = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.title