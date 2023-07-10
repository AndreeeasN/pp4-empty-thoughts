from django import forms
from .models import Tag


# Used in thought forms for adding tags
class TagWidget(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = Tag.objects.all().values_list('id', 'name')
