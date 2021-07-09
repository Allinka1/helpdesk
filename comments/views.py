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
    template_name = "comments/comment_form.html"
    success_url = reverse_lazy("request:list")

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()

        return super(CommentCreateView, self).form_valid(form)
