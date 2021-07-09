from django.urls import path

from comments.views import (CommentCreateView, )

app_name = "comments"
urlpatterns = [
    path("create_comment/", CommentCreateView.as_view(), name="create"),
]
