
from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    """
    Custom permission to only allow users with a specific condition.
    """
    def MyPermissions(self, request, view):
        if request.method == 'GET':
            # Allow read-only methods for all users
            return True
        # Example condition: allow access only if the user is authenticated
        return False