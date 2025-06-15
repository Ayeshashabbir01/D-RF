from .models import Student
from rest_framework import serializers  # type: ignore




class StudentSerializer(serializers.ModelSerializer):
     # validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']


    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'iqra' and ct.lower() != 'Sdk':
            raise serializers.ValidationError('City must be Kot samaba')
        return data

    
 