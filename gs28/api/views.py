from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly






class StudentModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
   
    #permission_classes = [IsAuthenticated]  # Uncomment this line to require authentication for all actions   
    permission_classes = [IsAuthenticatedOrReadOnly]
