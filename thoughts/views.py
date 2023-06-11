from django.shortcuts import render, redirect
from .models import Thought
from .forms import ThoughtForm

# Create your views here.


def get_thoughts(request):
    thoughts = Thought.objects.all()
    context = {
        'thoughts': thoughts
    }

    return render(request, 'thoughts/view_thoughts.html', context)


def add_thought(request):
    if request.method == 'POST':
        Thought.objects.create(
            title=request.POST.get('thought_title'),
            author=request.User,
            content=request.POST.get('thought_content'),
            date=request.POST.get('thought_datetime'),
            anonymous='anonymous' in request.POST
            )
        return redirect('get_thoughts')
    form = ThoughtForm()
    context = {
        'form': form
    }
    return render(request, 'thoughts/add_thought.html', context)
