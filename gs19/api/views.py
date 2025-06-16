from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
