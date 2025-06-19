from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Custom authentication using a GET parameter ?USERNAME=.
        Example: /studentapi/?USERNAME=admin
        """
        username = request.GET.get('username') 
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('❌ User not found.')

        return (user, None)  # Authenticated user returned
