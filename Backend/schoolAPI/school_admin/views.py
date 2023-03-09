from django.shortcuts import render
from django.http import HttpResponse
from school_admin.models import Admin_class
from teacher.models import Teacher
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AdminSerializer,TeacherSerializer   #optional(only if use serializing process)


# Create your views here.

@api_view(['POST'])
def admin_login(request):

    a_username = request.POST['usernm']
    a_password = request.POST['psswrd']
    try:
        check = Admin_class.objects.get(username = a_username, password = a_password)
        status = True
    except:
        status=False
    return JsonResponse({'status':status})


@api_view(['POST'])   
def add_teacher(request):
    try:
        # print (request.data)
        teacher_data = request.data #request.data uses in POST method
        email_ex = Teacher.objects.filter(email = teacher_data['email']).exists()
        if not email_ex:
            serialised_data = TeacherSerializer(data = teacher_data)
            if serialised_data.is_valid():
                serialised_data.save()
                msg = 'Teacher added'
            else:
                msg = 'form error'
        else:
            msg = 'email already exists'
    except Exception as d:
        print(d)
        msg = 'Something  wrong !!!'

    return JsonResponse({'msg':msg})


@api_view(['GET'])
def view_teacher(request):
    teach_dt = Teacher.objects.all()
    serialised_dat = TeacherSerializer(teach_dt,many = True) # many = true use only when multiple raws are fetching
    return JsonResponse({'teacher':serialised_dat.data})

