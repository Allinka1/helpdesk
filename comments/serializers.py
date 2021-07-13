from rest_framework import serializers
from comments.models import Comment
from user.serializers import UserSerializer
from request.serializers import RequestSerializer


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    url_api = serializers.HyperlinkedIdentityField(
        view_name='api:comment:detail',
        lookup_field='pk'
    )

    user = UserSerializer(read_only=True)
    request = RequestSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id','body', 'user', 'request', 'url_api', 'created_at']
