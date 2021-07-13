from django.urls import path

from api.views.request import (RequestListAPIView, RequestDetailAPIView,
                               RequestCreateAPIView, RequestRestoredAPIView,
                               RequestConfirmAPIView, )

app_name = 'request'
urlpatterns = [
    path('', RequestListAPIView.as_view(), name='list'),
    path('<int:pk>/', RequestDetailAPIView.as_view(), name='detail'),
    path('create/', RequestCreateAPIView.as_view(), name='create'),
    path('restored/', RequestRestoredAPIView.as_view(), name='restored'),
    path('<int:pk>/confirm/', RequestConfirmAPIView.as_view(), name='confirm'),
    # path('reject/', RequestRejectAPIView.as_view(), name='reject'),
]
