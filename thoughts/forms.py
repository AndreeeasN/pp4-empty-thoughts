from django import forms
# from django.forms.widgets import TextInput
from .models import Thought, Comment, Tag


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content', 'time', 'anonymous', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'anonymous']

# class TagsForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = '__all__'
#         widget = {
#             'text_color': TextInput(attrs={'type': 'color'}),
#             'bg_color': TextInput(attrs={'type': 'color'}),
#         }
