"""
Purchase Application URLs Configuration
=======================================

"""

from django.urls import path

from request.views import (RequestCreateView, RequestDetailView,
                           RequestListView, RequestUpdateView,
                           FormUpdateView, )

app_name = "request"
urlpatterns = [
    path("create/", RequestCreateView.as_view(), name="create"),
    path("<int:pk>/", RequestDetailView.as_view(), name="detail"),
    path("", RequestListView.as_view(), name="list"),
    path("update/<int:pk>/", RequestUpdateView.as_view(), name="update"),
    path("change/<int:pk>/", FormUpdateView.as_view(), name="change"),
]
