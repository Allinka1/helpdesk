"""
Comment Application Models
===========================

"""

from django.db import models

class Comment(models.Model):
    """Comment model implementation"""

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False)
    request = models.ForeignKey("request.Request", on_delete=models.CASCADE, null=False)
    body = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __repr__(self):
        return f'<Comment ("{self.id}")>'

    def __str__(self):
        """Return a string version of an instance"""

        return self.body
