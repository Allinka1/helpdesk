from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserTest(TestCase):

    def setUp(self):
        User.objects.create(username='alina', password='password')

    def test_login(self):
        response = self.client.post('/login/', {'username': 'alina', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/login/?next=/logout/')
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("alina1", "alina@dev.io", "some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("request:list"))
        self.assertEqual(response.status_code, 200)
