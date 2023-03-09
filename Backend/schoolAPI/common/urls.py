from django.urls import path
from .import views
urlpatterns=[
    path('teacher_login',views.teacher_login)
]