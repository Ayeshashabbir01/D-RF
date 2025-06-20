from .models import Student
from rest_framework import serializers # type: ignore

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
      #  print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
      #  print(instance.roll)
        instance.city=validated_data.get('city',instance.city)
       # print(instance.city)
        instance.save()
        return instance