"""
Comment Application Forms

"""

from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    """Comment form implementation"""

    class Meta:
        model = Comment
        fields = ["request", "user", "body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 1, "id": "body:text"}),
            "request": forms.HiddenInput(),
            "user": forms.HiddenInput(),
        }
