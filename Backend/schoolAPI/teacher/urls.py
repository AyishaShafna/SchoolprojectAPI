from django.urls import path
from .import views
urlpatterns=[
    path('teacher_profile',views.teacher_profile)
]