from django.db import models

class Student(models.Model):
    Sno=models.IntegerField()
    Name=models.CharField(max_length=64)
    Age=models.IntegerField()
    Dep=models.CharField(max_length=64)
    
# Create your models here.
