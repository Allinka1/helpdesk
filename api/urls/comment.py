from django.urls import path

from api.views.comment import CommentListAPIView, CommentDetailAPIView

app_name = 'comments'
urlpatterns = [
    path('request/<int:request_pk>/comment/', CommentListAPIView.as_view(), name='list'),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view(), name='detail')
]
