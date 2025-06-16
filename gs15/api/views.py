from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import CreateAPIView ,ListAPIView,RetrieveAPIView,UpdateAPIView, DestroyAPIView, ListCreateAPIView ,RetrieveUpdateAPIView ,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView



class StudentList(ListAPIView):
    """
    API view to list all students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentCreate(CreateAPIView):
    """API view to create a new student.
    """ 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    """
    API view to retrieve a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentUpdate(UpdateAPIView):
    """API view to update a student by ID.
    """     
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDestroy(DestroyAPIView):
    """API view to delete a student by ID.
    """   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
    """
    API view to list all students and create a new student.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    """
    API view to retrieve and update a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    """
    API view to retrieve and delete a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, and delete a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer