from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Page(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.SET_NULL)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    page_title=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()