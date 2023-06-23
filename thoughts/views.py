from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from .models import Thought, User
from .forms import ThoughtForm


class ThoughtList(generic.ListView):
    model = Thought
    queryset = Thought.objects.order_by('-date_created')
    template_name = 'thoughts/view_thoughts.html'
    paginate_by = 4

    def add_thought(request):
        if request.method == 'POST':
            form = ThoughtForm(request.POST)
            if form.is_valid():
                # Sets the author to current user before saving
                temp_form = form.save(commit=False)
                temp_form.author = request.user
                temp_form.save()
                return redirect('home')
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
                return redirect('home')
        form = ThoughtForm(instance=thought)
        context = {
            'form': form
        }
        return render(request, 'thoughts/edit_thought.html', context)

    def delete_thought(request, thought_id):
        thought = get_object_or_404(Thought, id=thought_id)
        thought.delete()
        return redirect('home')


class ThoughtDetail(View):

    def get(self, request, *args, **kwargs):
        thought_id = kwargs.get('thought_id')
        queryset = Thought.objects
        thought = get_object_or_404(queryset, id=thought_id)
        comments = thought.comment_thought.order_by('date_created')
        liked = False
        if thought.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
                "thought": thought,
                "comments": comments,
                "liked": liked
            }
        return render(request, "thoughts/thought_detail.html", context)


class UserDetail(User):
    def view_user(request, user_id):
        user = get_object_or_404(User, id=user_id)
        context = {
            'user': user
        }
        return render(request, 'users/view_user.html', context)
