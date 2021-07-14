from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, DetailView,
                                  UpdateView)
from request.models import Request
from request.forms import RequestForm, RequestUpdateForm
from comments.forms import CommentForm


def check_user(user, user_request):
    if user != user_request.user and not user.is_staff:
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
    paginate_by = 5

    def get_queryset(self):
        queryset = super(RequestListView, self).get_queryset()

        if self.request.user.is_staff:
            return queryset.filter(status=1)
        else:
            return queryset.filter(user=self.request.user)


class RequestDetailView(LoginRequiredMixin, DetailView):
    """Request detail view implementation"""

    model = Request
    template_name = "request/request_detail.html"

    def get(self, request, *args, **kwargs):
        """Handle GET request"""

        check_user(request.user, self.get_object())

        return super(RequestDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestDetailView, self).get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            initial_data = {
                "request": self.get_object(),
                "user": user
            }
            context["form"] = CommentForm(initial=initial_data)

        return context


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    """Request Update view implementation"""

    model = Request
    http_method_names = ["post"]
    exclude = ["__all__"]
    success_url = "/"

    def post(self, request, *args, **kwargs):
        """Handle Request update status"""

        request = Request.objects.all().filter(id=kwargs['pk'])
        request.update(status=4)
        return super(RequestUpdateView, self).post(request, *args, **kwargs)


class FormUpdateView(LoginRequiredMixin, UpdateView):
    """Form Update view implementation"""

    model = Request
    form_class = RequestUpdateForm
    template_name = "request/request_form.html"
    success_url = reverse_lazy("request:list")
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        """Prohibit admin updating request"""
        if self.request.user.is_staff:
            raise PermissionDenied

        return super(FormUpdateView, self).get(request, *args, **kwargs)
