''' Request Application Rest API View '''

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,
                                     CreateAPIView, )
from rest_framework.mixins import CreateModelMixin

from request.models import Request
from request.serializers import RequestSerializer, RequestUpdateSerializer

import pdb
class RequestListAPIView(ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if self.request.query_params.get('priority') != None:
            queryset = Request.objects.filter(priority=self.request.query_params.get('priority'))
        else:
            queryset = Request.objects.all()

        if user.is_staff:
            queryset = queryset.filter(status=1)
        else:
            queryset = queryset.filter(user_id=user.id)
        return queryset

    serializer_class = RequestSerializer


class RequestDetailAPIView(RetrieveUpdateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Request.objects.filter(user_id=user.id)
    serializer_class = RequestUpdateSerializer
    lookup_url_kwargs = 'pk'
    lookup_fields = 'pk'


class RequestCreateAPIView(CreateAPIView, CreateModelMixin):
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestRestoredAPIView(ListCreateAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Request.objects.filter(status=4)


class RequestConfirmAPIView(CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_url_kwargs = 'pk'
    lookup_fields = 'pk'


    def perform_create(self, serializer):
        user = self.request.user
        if user.is_staff:
            serializer.save(status=2)
