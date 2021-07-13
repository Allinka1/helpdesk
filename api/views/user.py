from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from user.serializers import UserSerializer
from api.permitions import UserAPIPermition, UserListAPIPermition


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserListAPIPermition]


class UserRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserAPIPermition]
