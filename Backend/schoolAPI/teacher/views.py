from django.shortcuts import render
from django.http import HttpResponse
from teacher.models import Teacher
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TeacherSerializer 

# Create your views here.
@api_view(['GET'])
def teacher_profile(request):
    params = request.GET # request.GET uses in GET method
    teacher_data = Teacher.objects.get(id = params['teacher_i'])
    serialised_data = TeacherSerializer(teacher_data)
    return JsonResponse({'teacher_d': serialised_data.data})
    
