from rest_framework import serializers
from .models import Student
# Create your serializers here.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # fields = '__all__'  # Uncomment this line to include all fields