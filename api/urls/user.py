from django.urls import path
from api.views.user import UserListAPIView, UserRetriveUpdateAPIView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'
urlpatterns = [
    path('<int:pk>/', UserRetriveUpdateAPIView.as_view(), name='detail'),
    path('', UserListAPIView.as_view(), name='list'),
    path('api-auth-token/', obtain_auth_token, name='auth-token'),
]
