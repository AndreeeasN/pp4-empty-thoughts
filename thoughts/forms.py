from django import forms
# from django.forms.widgets import TextInput
from .models import Thought, Comment, Tag
from thoughts.widgets import TagWidget, TimeWidget


class ThoughtForm(forms.ModelForm):
    """
    Form for submitting thoughts, uses crispyforms
    """
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=TagWidget,
        required=False
        )

    time = forms.TimeField(
        widget=TimeWidget,
        required=False
    )

    class Meta:
        model = Thought
        fields = ['title', 'content', 'time', 'anonymous', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'anonymous']
