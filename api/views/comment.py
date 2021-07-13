''' Comments Application Rest API View '''

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentListAPIView(ListCreateAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(request_id=self.kwargs['request_pk'])
        return queryset

    serializer_class = CommentSerializer


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
