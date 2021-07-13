""" Check authtoken expiration """

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from datetime import timedelta
from django.utils import timezone
from helpdeskapp.settings import TOKEN_EXPIRED_AFTER_SECONDS


class ExpiringTokenAuthentication(TokenAuthentication):
    def handle_token(self, token):
        """Delete or update token"""
        if self.is_expired(token):
            token.delete()
            raise AuthenticationFailed('The token is expired')
        token.created = timezone.now()
        token.save()
        return token

    def is_expired(self, token):
        """Check token expiration"""
        time_elapsed = timezone.now() - token.created
        expire = timedelta(
            seconds=TOKEN_EXPIRED_AFTER_SECONDS
        )
        return time_elapsed > expire

    def authenticate_credentials(self, key):
        """Get token from DB"""
        try:
            token = Token.objects.get(key=key)
            self.handle_token(token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid Token')

        return (token.user, token)
