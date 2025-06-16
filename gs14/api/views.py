from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin,
    RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)

# List and Create  -pk is not required
class LCStudentAPI(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve View ,Update View,# Delete View -pk is required
class RUDStudentAPI(RetrieveModelMixin, GenericAPIView ,UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Update View
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
# Delete View

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  