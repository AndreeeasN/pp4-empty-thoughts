from . import views
from django.urls import path


urlpatterns = [
    path('', views.ThoughtList.as_view(), name='home'),
    path('add', views.ThoughtList.add_thought, name='add'),
    path('edit/<thought_id>', views.ThoughtList.edit_thought, name='edit'),
    path(
        'delete/<thought_id>',
        views.ThoughtList.delete_thought,
        name='delete'
        ),
    path(
        'like/<thought_id>',
        views.ThoughtList.like_toggle_thought,
        name='like'
        ),
    path('view/<thought_id>', views.ThoughtDetail.as_view(), name='view'),
    path(
        'like_comment/<comment_id>',
        views.ThoughtDetail.like_toggle_comment,
        name='like_comment'
        ),
    path(
        'delete_comment/<comment_id>',
        views.ThoughtDetail.delete_comment,
        name='delete_comment'
        ),
    path('search/', views.ThoughtList.search, name='search'),
]
