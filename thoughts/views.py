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
    paginate_by = 8

    def get_queryset(self):
        """
        Filters the default queryset using filters.ThoughtFilter
        """
        queryset = super().get_queryset()
        thought_filter = ThoughtFilter(self.request.GET, queryset=queryset)
        return thought_filter.qs

    def get_context_data(self, **kwargs):
        """
        Sets context to include thoughtFilter,
        allows us to include details of our search
        """
        context = super().get_context_data(**kwargs)
        thought_filter = ThoughtFilter(
            self.request.GET,
            queryset=self.get_queryset()
            )
        context['filter'] = thought_filter
        return context

    def add_thought(request):
        """
        Creates a new thought using the contents of ThoughtForm
        with the logged in user as the author
        """
        if not user_is_logged_in(request.user):
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to post thoughts.'
                )
            return redirect('account_login')

        if request.method == 'POST':
            form = ThoughtForm(request.POST)
            if form.is_valid():
                # Sets the author to current user before saving
                thought = form.save(commit=False)
                thought.author = request.user
                thought.save()
                # Saves tags (many-to-many relationship)
                form.save_m2m()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Thought successfully posted!'
                    )
                return redirect('home')
        form = ThoughtForm()
        context = {
            'form': form
        }
        return render(request, 'thoughts/add_thought.html', context)

    def edit_thought(request, thought_id):
        """
        Edits an existing thought with the specified id
        using the form ThoughtForm
        """
        thought = get_object_or_404(Thought, id=thought_id)

        # Ensures only the owner/superuser may edit
        if not user_is_owner_or_superuser(request.user, thought.author):
            messages.add_message(
                request,
                messages.ERROR,
                'Only the owner may edit this post.'
                )
            return redirect('home')

        if request.method == 'POST':
            form = ThoughtForm(request.POST, instance=thought)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Thought successfully edited.'
                    )
                return redirect('home')
        form = ThoughtForm(instance=thought)
        context = {
            'form': form
        }
        return render(request, 'thoughts/edit_thought.html', context)

    def delete_thought(request, thought_id):
        """
        Deletes thought with the specified id
        """
        thought = get_object_or_404(Thought, id=thought_id)

        # Ensures only the owner/superuser may delete
        if not user_is_owner_or_superuser(request.user, thought.author):
            messages.add_message(
                request,
                messages.ERROR,
                'Only the owner may delete this post.'
                )
        else:
            thought.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Post successfully deleted.'
                )
        return redirect('home')

    def like_toggle_thought(request, thought_id):
        """
        Adds user to 'likes' of specified thought,
        if already present removes user instead
        """
        thought = get_object_or_404(Thought, id=thought_id)
        user = request.user
        # If not logged in, redirects to login page
        if not user_is_logged_in(user):
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to leave likes.'
                )
            return redirect('account_login')

        if thought.likes.filter(id=user.id).exists():
            thought.likes.remove(user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Succesfully unliked a post!'
                )
        else:
            thought.likes.add(user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Succesfully liked a post!'
                )
        return redirect('home')


class ThoughtDetail(View):
    """
    Displays a single thought and related comments
    """
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
        """
        Posts a comment on the thought with
        the logged in user as the comment author
        """
        # Ensures user is logged in, redirects to login
        if not user_is_logged_in(request.user):
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
                request, messages.SUCCESS,
                'Successfully left a comment.'
                )
            return redirect(f'../view/{comment.thought.pk}')
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
        # Ensures user is logged in, else redirects to login page
        if not user_is_owner_or_superuser(user, comment.author):
            messages.add_message(
                request,
                messages.ERROR,
                'Please sign in to leave likes.'
                )
            return redirect('account_login')

        if comment.likes.filter(id=user.id).exists():
            comment.likes.remove(user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Succesfully unliked a comment!'
                )
        else:
            comment.likes.add(user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Succesfully liked a comment!'
                )
        return redirect(f'../view/{comment.thought.pk}')

    def delete_comment(request, comment_id):
        """
        Deletes comment with specified id
        """
        comment = get_object_or_404(Comment, id=comment_id)

        # Ensures only the owner/superuser may delete
        if not user_is_owner_or_superuser(request.user, comment.author):
            messages.add_message(
                request,
                messages.ERROR,
                'Only the owner may delete this comment.'
                )
        else:
            comment.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment successfully deleted.'
                )
        return redirect(f'../view/{comment.thought.pk}')


class UserDetail(User):
    """
    Display a user profile containing the amount of
    posts and likes given/received by a specified user
    """
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


def user_is_logged_in(user):
    """
    Used to check if specified user is
    authenticated and not anonymousUser
    """
    return user.is_authenticated and not user.is_anonymous


def user_is_owner_or_superuser(user, object_owner):
    """
    Used to check if user is the owner
    of an object or is a superuser
    """
    return user is object_owner or user.is_superuser
