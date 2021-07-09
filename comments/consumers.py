"""
Comments Application Consumers
===========================

"""
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

from request.models import Request
from comments.models import Comment
from django.core.exceptions import PermissionDenied


class CommentRequestConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_id = None

    async def connect(self):
        self.request_id = self.scope["url_route"]["kwargs"]["id"]

        await self.channel_layer.group_add(
            self.request_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.request_id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json.get("body")

        new_comment = await self.create_new_comment(body)
        datetime_format = "%b %d, %Y, %I:%M %p"
        await self.channel_layer.group_send(
            self.request_id,
            {
                "type": "new_comment",
                "user": new_comment.user.username,
                "created_at": new_comment.created_at.strftime(datetime_format),
                "body": new_comment.body,
            }
        )

    async def request_comment(self, event):
        body = event.get("body")

        await self.send(text_data=json.dumps({
            "body": body,
            "user": self.scope["user"].username,
            "created_at": timezone.now().strftime("%b %d, %Y, %H:%M")
        }))

    async def new_comment(self, event):
        body = event.get("body")
        user = event.get("user")
        created_at = event.get("created_at")

        await self.send(text_data=json.dumps({
            "body": body,
            "user": user,
            "created_at": created_at,
        }))

    @database_sync_to_async
    def create_new_comment(self, body):
        request = Request.objects.get(id=self.request_id)
        if request.status != "active":
            raise PermissionDenied
        return Comment.objects.create(
            user=self.scope["user"],
            request=request,
            body=body
        )
