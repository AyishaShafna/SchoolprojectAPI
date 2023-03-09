from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    age = models.BigIntegerField()
    gender = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 200)
    phone = models.BigIntegerField()
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

class Meta:
    db_table = 'teacher_tbl'
