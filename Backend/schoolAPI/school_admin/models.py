from django.db import models

# Create your models here.
class Admin_class(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Meta:
    db_table = 'admin_tb'