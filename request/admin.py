"""
Request Application Administration
================================

"""

from django.contrib import admin
from django.contrib import messages

from request.models import Request, RestoredRequest
from django.http import HttpResponseRedirect


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """Request admin implementation"""

    change_form_template = "admin/request/change_form.html"

    def response_change(self, request, obj):
        """Change request status implementation"""
        if "_confirm" in request.POST:
            obj.status = 2
            obj.save()
            self.message_user(request, "Successfully confirmed")
            return HttpResponseRedirect(".")
        if "_reject" in request.POST:
            if len(obj.reject_message) == 0:
                self.message_user(request, "Please fill the reject message", level=messages.ERROR)
            else:
                obj.status = 3
                obj.save()
                self.message_user(request, "Successfully rejected")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    readonly_fields = [
        "status",
        "priority",
        "user",
        "title",
        "description",
    ]

    list_display = [
        "status",
        "priority",
        "title",
        "user",
        "created_at",
    ]

    list_display_links = [
        "title",
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=1)


@admin.register(RestoredRequest)
class RestoredRequestAdmin(admin.ModelAdmin):
    """Restored Request admin implementation"""

    change_form_template = "admin/request/change_form.html"

    def response_change(self, request, obj):
        """Change request status implementation"""
        if "_confirm" in request.POST:
            obj.status = 2
            obj.save()
            self.message_user(request, "Successfully confirmed")
            return HttpResponseRedirect(".")
        if "_reject" in request.POST:
            if len(obj.reject_message) == 0:
                self.message_user(request, "Please fill the reject message", level=messages.ERROR)
            else:
                obj.status = 3
                obj.save()
                self.message_user(request, "Successfully rejected")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    readonly_fields = [
        "status",
        "priority",
        "user",
        "title",
        "description",
    ]

    list_display = [
        "status",
        "priority",
        "title",
        "user",
        "created_at",
    ]

    list_display_links = [
        "title",
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=4)
