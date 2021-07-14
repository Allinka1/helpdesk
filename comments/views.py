from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.


class CommentCreateView(LoginRequiredMixin, CreateView):
    """Comment create view implementation"""

    model = Comment
    form_class = CommentForm
    template_name = "comment/comment_form.html"
    success_url = reverse_lazy("request:list")
