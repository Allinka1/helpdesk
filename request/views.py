from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from request.models import Request
from request.forms import RequestForm
import pdb


def check_user(user, user_request):
    if user != user_request.user:
        raise PermissionDenied


class RequestCreateView(LoginRequiredMixin, CreateView):
    """Request create view implementation"""

    model = Request
    form_class = RequestForm
    template_name = "request/request_form.html"
    success_url = reverse_lazy("request:list")

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()

        return super(RequestCreateView, self).form_valid(form)


class RequestListView(LoginRequiredMixin, ListView):
    """Request list view implementation"""

    model = Request
    template_name = "request/request_list.html"

    def get_queryset(self):
        queryset = super(RequestListView, self).get_queryset()

        return queryset.filter(user=self.request.user)


class RequestDetailView(LoginRequiredMixin, DetailView):
    """Request detail view implementation"""

    model = Request
    template_name = "request/request_detail.html"

    def get(self, request, *args, **kwargs):
        """Handle GET request"""

        check_user(request.user, self.get_object())

        return super(RequestDetailView, self).get(request, *args, **kwargs)


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    """Request delete view implementation"""

    model = Request
    template_name = "request/request_delete.html"
    success_url = reverse_lazy("request:list")

    def post(self, request, *args, **kwargs):
        """Handle POST request"""

        check_user(request.user, self.get_object())

        return super(RequestDeleteView, self).post(request, *args, **kwargs)
