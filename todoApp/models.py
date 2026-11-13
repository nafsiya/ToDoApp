from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200,null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    status=models.CharField(max_length=100,default="pending")
    
    
    
    