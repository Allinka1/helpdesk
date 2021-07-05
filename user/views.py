from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from user.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "auth/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "auth/login.html"

    def get_success_url(self):

        return reverse_lazy("request:list")


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        logout(self.request)

        redirect_url = reverse_lazy("login")
        return HttpResponseRedirect(redirect_url)
