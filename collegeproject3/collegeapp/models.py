from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.dname
class Branch(models.Model):
    bname=models.CharField(max_length=250,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.bname

class Applicationform(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    date    = models.CharField(max_length=100)
    gender  = models.CharField(max_length=100)
    age     = models.CharField(max_length=100)
    phone   = models.CharField(max_length=100)
    email   = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    materials_provide = models.TextField()
    Branch_id = models.ForeignKey(Branch , on_delete=models.CASCADE)
    Department_id = models.ForeignKey(Department , on_delete=models.CASCADE)