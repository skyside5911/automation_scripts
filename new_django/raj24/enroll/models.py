from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stumail = models.EmailField(max_length=100)
    stupass = models.CharField(max_length=100)