from rest_framework import serializers
from school_admin.models import Admin_class
from teacher.models import Teacher

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_class
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Teacher
        fields = '__all__'