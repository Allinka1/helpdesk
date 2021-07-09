"""
Comments Application ASGI Routing
==============================

"""

from django.urls import re_path

from comments.consumers import CommentRequestConsumer

websocket_urlpatterns = [
    re_path(r"(?P<id>\d+)/$", CommentRequestConsumer.as_asgi()),
]
