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

    def filter_search_text(self, queryset, _name, value):
        """
        Returns combined title/content query
        """
        return queryset.filter(
            Q(title__icontains=value) |
            Q(content__icontains=value)
            )

    def filter_author(self, queryset, _name, value):
        """
        Excludes anonymous posts from query if searching by author
        """
        if value:
            queryset = queryset.exclude(anonymous=True)
        return queryset.filter(author__username__icontains=value)

    def filter_tags(self, queryset, _name, value):
        """
        Filter query by tags if tags have been entered
        """
        if value:
            for tag in value:
                queryset = queryset.filter(tags=tag)
        return queryset

    def is_searching(self):
        """
        Returns true if any of the 3 fields aren't empty
        """
        return (
            self.data.get('search_text') or
            self.data.get('author') or
            self.data.get('tags')
        )

    class Meta:
        model = Thought
        fields = ['search_text', 'author']
