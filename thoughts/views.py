from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Thought, User
from .forms import ThoughtForm, CommentForm


class ThoughtList(generic.ListView):
    model = Thought
    queryset = Thought.objects.order_by('-date_created')
    template_name = 'thoughts/view_thoughts.html'
    paginate_by = 10

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
                "liked": liked,
                "comment_form": CommentForm(),
            }
        return render(request, "thoughts/thought_detail.html", context)

    def post(self, request, *args, **kwargs):
        # Safeguard for if user somehow manages to write a
        # comment without being logged in, redirects to login page
        if not request.user.is_authenticated or request.user.is_anonymous:
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to leave comments.'
                )
            return redirect('account_login')

        thought_id = kwargs.get('thought_id')
        queryset = Thought.objects
        thought = get_object_or_404(queryset, id=thought_id)
        comments = thought.comment_thought.order_by('date_created')
        liked = False
        if thought.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.thought = thought
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.INFO,
                'Successfully left a comment.'
                )
        else:
            comment_form = CommentForm()
            messages.add_message(
                request, messages.ERROR,
                'Comment was not posted.'
                )

        context = {
                "thought": thought,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        return render(request, "thoughts/thought_detail.html", context)


class UserDetail(User):
    def view_user(request, user_id):
        user = get_object_or_404(User, id=user_id)
        context = {
            'user': user
        }
        return render(request, 'users/view_user.html', context)
