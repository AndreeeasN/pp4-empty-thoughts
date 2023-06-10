from django.shortcuts import render
from .models import Thought

# Create your views here.


def get_thoughts(request):
    thoughts = Thought.objects.all()
    context = {
        'thoughts': thoughts
    }

    return render(request, 'thoughts/view_thoughts.html', context)
