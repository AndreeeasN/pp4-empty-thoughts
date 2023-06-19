from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from .models import Thought

# Create your tests here.


class TestViews(TestCase):
    """
    Used to test various Views, the first three test were taken
    from the Code Institute "Hello Django" Codealong project
    """
    def test_view_thoughts_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thoughts/view_thoughts.html')

    def test_add_thoughts_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thoughts/add_thought.html')

    def test_edit_thoughts_page(self):
        user = get_user_model().objects.create(username='TestAccount')
        thought = Thought.objects.create(author=user)
        response = self.client.get(f'/edit/{thought.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thoughts/edit_thought.html')

    def test_can_add_thought(self):
        # Requires a logged in user to add thought
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='TestAccount',
            password='123'
            )
        self.client.login(username='TestAccount', password='123')
        response = self.client.post('/add', {
            'title': ['Test Title'],
            'content': ['Test Content'],
            'time': ['20:50:36'], 
            'initial-time': ['20:50:36'],
            })
        self.assertRedirects(response, '/')

    def test_can_delete_thought(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='TestAccount',
            password='123'
            )
        self.client.login(username='TestAccount', password='123')

        # Creating a thought requires logged in user and content
        thought = Thought.objects.create(
            author=self.user,
            content='Test Content'
        )
        response = self.client.get(f'/delete/{thought.id}')
        self.assertRedirects(response, '/')
        existing_items = Thought.objects.filter(id=thought.id)
        self.assertEqual(len(existing_items), 0)
