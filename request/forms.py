"""
Request Application Forms

"""

from django import forms

from request.models import Request


class RequestForm(forms.ModelForm):
    """Request form implementation"""

    class Meta:
        model = Request
        fields = ["priority", "title", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class RequestUpdateForm(RequestForm):
    """Request update form implementation"""
    class Meta:
        model = Request
        fields = ["priority", "description"]
