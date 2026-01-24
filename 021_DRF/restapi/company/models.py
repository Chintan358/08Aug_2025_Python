from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=20)
    hod = models.CharField(max_length=20)

class Emp(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()