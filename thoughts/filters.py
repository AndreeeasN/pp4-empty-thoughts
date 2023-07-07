from django.db.models import Q
from .models import Thought, Tag
from .widgets import TagWidget
import django_filters


class ThoughtFilter(django_filters.FilterSet):
    """
    Django-filter used for searching through posts
    """
    search_text = django_filters.CharFilter(
        method='filter_search_text',
        label='Search text:',

    )
    author = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        method='filter_author',
        label='Author:'
    )
    # Tags use our custom select2 TagWidget
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=TagWidget,
        method='filter_tags',
        label='Tags:'
    )

    # Combines title/content query to ease search
    def filter_search_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(content__icontains=value)
            )

    def filter_author(self, queryset, name, value):
        # Excludes anonymous posts if searching by author
        if value:
            queryset = queryset.exclude(anonymous=True)
        return queryset.filter(author__username__icontains=value)

    def filter_tags(self, queryset, name, value):
        # Only filter by tags if tags have been entered
        if value:
            # distinct() ensures we get no duplicate results
            queryset = queryset.filter(tags__in=value).distinct()
        return queryset

    class Meta:
        model = Thought
        fields = ['search_text', 'author']
