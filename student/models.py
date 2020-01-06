from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.TextField()
    Std=models.IntegerField()
    Age=models.IntegerField()
    