from django_select2 import forms as s2forms


# Used in thought forms for adding tags
class TagWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains"
    ]
    attrs = {'class': 'tag-widget'}
    allow_multiple_selected = True
