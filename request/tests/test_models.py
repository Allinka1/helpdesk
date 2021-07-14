from django.contrib.auth.models import User
from request.models import Request
from django.test import TestCase


class RequestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', email='test@mail.com', password='test')
        Request.objects.create(title='test title', description='test descr', user=user)

    def test_title_max_length(self):
        request = Request.objects.get(id=1)
        max_length = request._meta.get_field('title').max_length
        self.assertEquals(max_length, 55)

    def test_status_choices(self):
        request = Request.objects.get(id=1)
        status_choices = request._meta.get_field('status').choices
        self.assertEquals(status_choices, Request.REQUEST_STATUSES)

    def test_priority_choices(self):
        request = Request.objects.get(id=1)
        priority_choices = request._meta.get_field('priority').choices
        self.assertEquals(priority_choices, Request.PRIORITIES)

    def test_reject_message_null(self):
        request = Request.objects.get(id=1)
        null = request._meta.get_field('reject_message').null
        self.assertEquals(null, True)

    def test_user_null(self):
        request = Request.objects.get(id=1)
        null = request._meta.get_field('user').null
        self.assertEquals(null, False)

    def test_title_null(self):
        request = Request.objects.get(id=1)
        null = request._meta.get_field('title').null
        self.assertEquals(null, False)

    def test_description_null(self):
        request = Request.objects.get(id=1)
        null = request._meta.get_field('description').null
        self.assertEquals(null, False)

    def test_created_at(self):
        request = Request.objects.get(id=1)
        created = request._meta.get_field('created_at').auto_now_add
        self.assertEquals(created, True)
