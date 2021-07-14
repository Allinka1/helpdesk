from django.contrib.auth.models import User
from request.models import Request
from comments.models import Comment
from django.test import TestCase


class RequestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', email='test@mail.com', password='test')
        request = Request.objects.create(title='test title', description='test descr', user=user)
        Comment.objects.create(user=user, request=request, body='test body')

    def test_body_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('body').max_length
        self.assertEquals(max_length, 100)

    def test_body_null(self):
        comment = Comment.objects.get(id=1)
        null = comment._meta.get_field('body').null
        self.assertEquals(null, False)

    def test_user_null(self):
        comment = Comment.objects.get(id=1)
        null = comment._meta.get_field('user').null
        self.assertEquals(null, False)

    def test_request_null(self):
        comment = Comment.objects.get(id=1)
        null = comment._meta.get_field('request').null
        self.assertEquals(null, False)
