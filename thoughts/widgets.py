from django import forms
from .models import Tag
from bootstrap_datepicker_plus.widgets import TimePickerInput


class TagWidget(forms.SelectMultiple):
    """
    Multi-select widget for adding tags,
    to be used with select2
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = Tag.objects.all()

    attrs = {'class': 'tagwidget'}
    is_required = False
    allow_multiple_selected = True


class TimeWidget(TimePickerInput):
    """
    Widget for selecting a time,
    formatted as Hours:Minutes
    """
    attrs = {'class': 'timewidget'}
    is_required = False
    options = {
        'format': 'HH:mm'
    }
