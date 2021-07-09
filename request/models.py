"""
Request Application Models
===========================

"""

from django.db import models


class Request(models.Model):
    """Request model implementation"""

    ACTIVE = 1
    CONFIRMED = 2
    REJECTED = 3
    RESTORED = 4


    REQUEST_STATUSES = [

        (ACTIVE, "Active"),
        (CONFIRMED, "Confirmed"),
        (REJECTED, "Rejected"),
        (RESTORED, "Restored"),
        
    ]

    LOW = 1
    MEDIUM = 2
    HIGH = 3


    PRIORITIES = [

        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),

    ]

    id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=REQUEST_STATUSES, default=1)
    priority = models.IntegerField(choices=PRIORITIES, default=1)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=55, null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reject_message = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = "request"
        verbose_name_plural = "requests"


    def __repr__(self):
        return f'<Request ("{self.id}") ("{self.status}")>'


class RestoredRequest(Request):
    """ Restored Request model implementation"""

    class Meta:
        proxy = True
