from django.urls import path

from api.views.request import (RequestListAPIView, RequestDetailAPIView,
                               RequestCreateAPIView,
                               RequestRestoredListAPIView,
                               RequestConfirmAPIView, RequestRejectAPIView,
                               RequestRestoredAPIView, )

app_name = 'request'
urlpatterns = [
    path('', RequestListAPIView.as_view(), name='list'),
    path('<int:pk>/', RequestDetailAPIView.as_view(), name='detail'),
    path('create/', RequestCreateAPIView.as_view(), name='create'),
    path('restored-list/', RequestRestoredListAPIView.as_view(), name='restored-list'),
    path('<int:pk>/confirm/', RequestConfirmAPIView.as_view(), name='confirm'),
    path('<int:pk>/reject/', RequestRejectAPIView.as_view(), name='reject'),
    path('<int:pk>/restored/', RequestRestoredAPIView.as_view(), name='restored'),
]
