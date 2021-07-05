"""
Purchase Application URLs Configuration
=======================================

"""

from django.urls import path

from request.views import (RequestCreateView, RequestDeleteView,
                           RequestDetailView, RequestListView, )

app_name = "request"
urlpatterns = [
    path("create/", RequestCreateView.as_view(), name="create"),
    path("<int:pk>/", RequestDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", RequestDeleteView.as_view(), name="delete"),
    path("", RequestListView.as_view(), name="list"),
]
