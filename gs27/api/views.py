from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [MyPermissions]
   