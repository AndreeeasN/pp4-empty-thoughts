from django import forms
from .models import Thought, Comment, Tag
from thoughts.widgets import TagWidget, TimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class ThoughtForm(forms.ModelForm):
    """
    Form for submitting thoughts, uses custom widgets
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-8 mb-0 px-1'),
                Column('time', css_class='form-group col-md-4 mb-0 px-1'),
                css_class='form-row'
            ),
            'content',
            'tags',
            'anonymous',
            Submit('submit', 'Submit Thought')
        )

    class Meta:
        model = Thought
        fields = ['title', 'content', 'time', 'anonymous', 'tags']
        widgets = {
            # Reduces size of text area
            'content': forms.Textarea(attrs={'rows': 4}),
            }


class CommentForm(forms.ModelForm):
    """
    Simple form for submitting comments
    """
    class Meta:
        model = Comment
        fields = ['content', 'anonymous']
        widgets = {
            # Reduces size of text area
            'content': forms.Textarea(attrs={'rows': 3}),
        }
