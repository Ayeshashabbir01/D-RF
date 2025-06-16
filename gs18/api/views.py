from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

