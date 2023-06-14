from django.shortcuts import get_object_or_404, render, redirect
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
        form = ThoughtForm(request.POST)
        if form.is_valid():
            # Sets the author to current user before saving
            temp_form = form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('get_thoughts')
    form = ThoughtForm()
    context = {
        'form': form
    }
    return render(request, 'thoughts/add_thought.html', context)


def edit_thought(request, thought_id):
    thought = get_object_or_404(Thought, id=thought_id)
    if request.method == 'POST':
        form = ThoughtForm(request.POST, instance=thought)
        if form.is_valid():
            form.save()
            return redirect('get_thoughts')
    form = ThoughtForm(instance=thought)
    context = {
        'form': form
    }
    return render(request, 'thoughts/edit_thought.html', context)


def delete_thought(request, thought_id):
    thought = get_object_or_404(Thought, id=thought_id)
    thought.delete()
    return redirect('get_thoughts')