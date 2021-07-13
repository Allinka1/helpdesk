''' Request Application Rest API View '''

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,
                                     CreateAPIView, )
from rest_framework.mixins import CreateModelMixin

from rest_framework import serializers

from request.models import Request
from request.serializers import (RequestSerializer, RequestUpdateSerializer,
                                 RequestUpdateStatusSerializer)

from django.core.exceptions import PermissionDenied


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


class RequestRestoredListAPIView(ListCreateAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Request.objects.filter(status=4)


class RequestConfirmAPIView(RetrieveUpdateAPIView):
    serializer_class = RequestUpdateStatusSerializer
    queryset = Request.objects.all()
    lookup_url_kwargs = 'pk'
    lookup_fields = 'pk'

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_staff:
            serializer.save(status=2)
        else:
            raise PermissionDenied


class RequestRejectAPIView(RetrieveUpdateAPIView):
    serializer_class = RequestUpdateStatusSerializer
    queryset = Request.objects.all()
    lookup_url_kwargs = 'pk'
    lookup_fields = 'pk'

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_staff:
            if serializer.validated_data.get('reject_message') == None:
                raise serializers.ValidationError('You must fill the reject message!')
            else:
                serializer.save(status=3)
        else:
            raise PermissionDenied


class RequestRestoredAPIView(RetrieveUpdateAPIView):
    serializer_class = RequestUpdateStatusSerializer
    queryset = Request.objects.filter(status=3)
    lookup_url_kwargs = 'pk'
    lookup_fields = 'pk'

    def perform_update(self, serializer):
        user = self.request.user
        if not user.is_staff:
            serializer.save(status=4)
        else:
            raise PermissionDenied
