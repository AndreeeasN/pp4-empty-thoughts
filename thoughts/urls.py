from . import views
from django.urls import path


urlpatterns = [
    path('', views.ThoughtList.as_view(), name='home'),
    path('add', views.ThoughtList.add_thought, name='add'),
    path('edit/<thought_id>', views.ThoughtList.edit_thought, name='edit'),
    path(
        'delete/<object_type>/<object_id>',
        views.ThoughtList.delete,
        name='delete'
        ),
    path(
        'like/<object_type>/<object_id>',
        views.ThoughtList.like_toggle,
        name='like'
        ),
    path('view/<thought_id>', views.ThoughtDetail.as_view(), name='view'),
]
