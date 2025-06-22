from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from api.throttling import JackRateThrottle  # Ensure this file exists
from rest_framework.authentication import SessionAuthentication # Make sure this file exists

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ UserRateThrottle, AnonRateThrottle]
    #throttle_classes = [JackRateThrottle, AnonRateThrottle]
