from django.db import models
# createsuperuser user:dell, password:Jyothi@11
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    father=models.CharField(max_length=50)

