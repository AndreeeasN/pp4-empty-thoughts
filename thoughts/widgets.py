from django import forms
from .models import Tag
from bootstrap_datepicker_plus.widgets import TimePickerInput


# Used in thought forms for adding tags
class TagWidget(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = Tag.objects.all()

    attrs = {'class': 'tagwidget'}
    is_required = False
    allow_multiple_selected = True


# Used in thought forms for time
class TimeWidget(TimePickerInput):
    attrs = {'class': 'timewidget'}
    is_required = False
    options = {
        'format': 'HH:mm'
    }
