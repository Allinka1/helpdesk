from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from request.models import Request


class RequestCreateViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='alina', password='password')
        self.client.force_login(user=user)

    def test_request_create_post(self):
        data = {
            'title': 'Test new title',
            'description': 'test new descr'
        }
        response = self.client.post(reverse('request:create'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_request_create_get(self):
        response = self.client.get(reverse('request:create'))
        self.assertTemplateUsed(response, "request/request_form.html")
        self.assertEqual(response.status_code, 200)


class RequestListViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='alina', password='password')
        Request.objects.create(user=user, title='title', description='test descr')
        self.client.force_login(user=user)

    def test_request_list(self):
        user = User.objects.first()
        response = self.client.get(reverse('request:list'))
        queryset = Request.objects.filter(user_id=user.id)
        self.assertTemplateUsed(response, "request/request_list.html")
        self.assertQuerysetEqual(response.context['request_list'], queryset)
        self.assertEqual(response.status_code, 200)


class RequestDetailViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='alina', password='password')
        Request.objects.create(user=user, title='title', description='test descr')
        self.client.force_login(user=user)

    def test_request_detail(self):
        request = Request.objects.last()
        response = self.client.get(reverse('request:detail', kwargs={'pk': request.id}))
        self.assertTemplateUsed(response, "request/request_detail.html")
        self.assertEqual(response.context['object'], request)
        self.assertEqual(response.status_code, 200)


class RequestFormUpdateViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='alina', password='password')
        Request.objects.create(user=user, title='title', description='test descr')
        self.client.force_login(user=user)

    def test_request_form_update_get(self):
        request = Request.objects.last()
        response = self.client.get(reverse('request:change', kwargs={'pk': request.id}))
        self.assertEqual(response.context['object'], request)
        self.assertTemplateUsed(response, "request/request_form.html")
        self.assertEqual(response.status_code, 200)

    def test_request_form_update_post(self):
        request = Request.objects.last()
        response = self.client.post(
            reverse('request:change', kwargs={'pk': request.id}),
            data={'description': 'test new descr'},
        )
        self.assertTemplateUsed(response, "request/request_form.html")
        self.assertEqual(response.status_code, 200)
