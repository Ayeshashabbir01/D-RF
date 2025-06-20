from .models import Student
from rest_framework import serializers # type: ignore


def start_with_r(value):
  if value[0].lower() != 'r':
     raise serializers.ValidationError('Name should be start with R')
         

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
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
    

  # field lavel validation
    def validate_roll(self,value):
     if value >= 200:
      raise serializers.ValidationError('seat full')
     return value
    
  

  # object level validation
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'falak' and ct.lower() != 'ryk':
        raise serializers.ValidationError('city must be ryk')
    return data
