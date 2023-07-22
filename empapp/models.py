from django.db import models

# Create your models here.
class EmpDetail(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    