from .filters import ThoughtFilter


def search_form(request):
    """
    Adds search_form to the context of every url,
    used to keep the search function available on every page
    """
    return {'search_form': ThoughtFilter(request.GET)}
