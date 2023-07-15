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
        widget=TagWidget(attrs={'id': 'form-tag-widget'}),
        required=False
        )

    time = forms.TimeField(
        widget=TimeWidget,
        required=False
    )

    class Meta:
        model = Thought
        fields = ['title', 'content', 'time', 'anonymous', 'tags']
        widgets = {
            # Reduces size of text area
            'content': forms.Textarea(attrs={'rows': 4}),
            }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'anonymous']
        widgets = {
            # Reduces size of text area
            'content': forms.Textarea(attrs={'rows': 3}),
        }
