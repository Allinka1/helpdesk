from django.test import TestCase
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
