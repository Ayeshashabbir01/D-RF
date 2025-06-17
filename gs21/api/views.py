from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]  # Change to AllowAny to allow unauthenticated access
    #permission_classes = [IsAdminUser]  # Change to IsAdminUser to restrict access to admin users only
    #permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access to unauthenticated users
    #permission_classes = [DjangoModelPermissions]  # Use Django's model permissions for access control
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Allows read-only access to unauthenticated users, but requires permissions for write operations