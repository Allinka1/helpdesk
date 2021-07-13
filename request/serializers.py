from rest_framework import serializers
from request.models import Request
from user.serializers import UserSerializer


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='request:detail',
        lookup_field='pk'
    )

    url_api = serializers.HyperlinkedIdentityField(
        view_name='api:request:detail',
        lookup_field='pk'
    )

    user = UserSerializer(read_only=True)
    status = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Request
        fields = '__all__'


class RequestUpdateSerializer(RequestSerializer):
    status = serializers.IntegerField(read_only=False)
    title = serializers.CharField(read_only=True)
