from django.db import models

# Create your models here.
class Student(models.Model):
    studentname= models.CharField(max_length=100)
    teachername= models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=200)