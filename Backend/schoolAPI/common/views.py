from django.shortcuts import render
from django.http import HttpResponse
from teacher.models import Teacher
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TeacherSerializer

# Create your views here.
@api_view(['POST'])
def teacher_login(request):
        t_email = request.POST['temail']
        t_pass = request.POST['tpassword']
        # login_data = request.data
        try:
            teacher = Teacher.objects.get(email = t_email, password = t_pass)
            status = True
            return JsonResponse({"status":status,"token":teacher.id}) # token set for session uses
        except:
            status = False

        return JsonResponse({"status":status})
    
