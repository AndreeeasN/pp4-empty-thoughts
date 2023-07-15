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
        widget=TagWidget(attrs={'id': 'search-tag-widget'}),
        method='filter_tags',
        label='Tags:',
    )

    # Combines title/content query to ease search
    def filter_search_text(self, queryset, _name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(content__icontains=value)
            )

    def filter_author(self, queryset, _name, value):
        # Excludes anonymous posts if searching by author
        if value:
            queryset = queryset.exclude(anonymous=True)
        return queryset.filter(author__username__icontains=value)

    def filter_tags(self, queryset, _name, value):
        # Only filter by tags if tags have been entered
        if value:
            for tag in value:
                queryset = queryset.filter(tags=tag)
        return queryset

    class Meta:
        model = Thought
        fields = ['search_text', 'author']
