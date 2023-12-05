from django.test import TestCase, Client
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(email='test@example.com', password='password123')
        self.assertEqual(user.email, 'test@example.com')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='test@example.com', password='password123')
        self.login_url = reverse('login')  

    def test_login_view(self):
        response = self.client.post(self.login_url, {'email': 'test@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  

