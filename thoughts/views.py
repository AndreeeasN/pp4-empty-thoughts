from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib import messages
from django.db.models import Sum
from .models import Thought, User, Comment
from .forms import ThoughtForm, CommentForm
from .filters import ThoughtFilter


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
                thought = form.save(commit=False)
                thought.author = request.user
                thought.save()
                # Saves tags (many-to-many relationship)
                form.save_m2m()
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

    def like_toggle_thought(request, thought_id):
        """
        Adds user to 'likes' of specified thought,
        if already present removes user instead
        """
        thought = get_object_or_404(Thought, id=thought_id)
        user = request.user
        # If not logged in, redirects to login page
        if not user.is_authenticated or user.is_anonymous:
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to leave likes.'
                )
            return redirect('account_login')

        if thought.likes.filter(id=user.id).exists():
            thought.likes.remove(user)
        else:
            thought.likes.add(user)
        return redirect('home')

    def search(request):
        thought_list = Thought.objects.all()
        thought_filter = ThoughtFilter(request.GET, queryset=thought_list)
        return render(
            request,
            'thoughts/search_thoughts.html',
            {"filter": thought_filter}
            )


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
        # Safeguard for if user manages to write a
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

    def like_toggle_comment(request, comment_id):
        """
        Adds user to 'likes' of specified comment,
        if already present removes user instead
        """
        comment = get_object_or_404(Comment, id=comment_id)
        user = request.user
        # If not logged in, redirects to login page
        if not user.is_authenticated or user.is_anonymous:
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to leave likes.'
                )
            return redirect('account_login')

        if comment.likes.filter(id=user.id).exists():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        return redirect(f'../view/{comment.thought.pk}')

    def delete_comment(request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect(f'../view/{comment.thought.pk}')


class UserDetail(User):
    def view_user(request, user_id):
        user = get_object_or_404(User, id=user_id)

        # All likes on user thoughts +  comments
        likes_given = user.thought_likes.all().count()
        + user.comment_likes.all().count()

        # Returns the amount of likes from the user posts/comments
        thought_likes = user.thoughts.aggregate(
            Sum('likes')
            )['likes__sum']
        comment_likes = user.comment_author.aggregate(
            Sum('likes')
            )['likes__sum']
        # int(value or 0) as safeguard, can return Nonetype if empty
        likes_received = int(thought_likes or 0) + int(comment_likes or 0)

        context = {
            'user_detail': user,
            'likes_given': likes_given,
            'likes_received': likes_received
        }
        return render(request, 'users/view_user.html', context)
