from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView



class StudentListCreate(ListCreateAPIView):
    """
    API view to list all students and create a new student.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, and delete a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer