from django.db import models

# Create your models here.
class Examcenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
class MyExamcenter(Examcenter):
    class Meta:
        proxy = True
        ordering = ['-id']
    
    