from django.shortcuts import render # type: ignore
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer  # type: ignore
from django .http import HttpResponse ,JsonResponse # type: ignore

# Model Object Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)  
    serializer = StudentSerializer(stu)  
    json_data = JSONRenderer().render(serializer.data)  
    return HttpResponse(json_data, content_type='application/json')  
    #return JsonResponse(serializer.data)

# Query Set - All Student Data 
def student_list(request):
    stu = Student.objects.all()  
    serializer = StudentSerializer(stu, many=True)  
    json_data = JSONRenderer().render(serializer.data)  
    return HttpResponse(json_data, content_type='application/json') 
    #return JsonResponse(serializer.data,safe=False )