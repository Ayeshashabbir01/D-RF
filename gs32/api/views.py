from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import CreateAPIView ,ListAPIView,RetrieveAPIView,UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle



class StudentList(ListAPIView):
    """
    API view to list all students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'viewstu'
class StudentCreate(CreateAPIView):
    """API view to create a new student.
    """ 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'modifystu'
class StudentRetrieve(RetrieveAPIView):
    """
    API view to retrieve a student by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'viewstu'
class StudentUpdate(UpdateAPIView):
    """API view to update a student by ID.
    """     
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'modifystu'
class StudentDestroy(DestroyAPIView):
    """API view to delete a student by ID.
    """   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'modifystu'

