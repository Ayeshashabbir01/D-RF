from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]  # Change to AllowAny to allow unauthenticated access
    permission_classes = [IsAdminUser]  # Change to IsAdminUser to restrict access to admin users only

