from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
        # return "hi"
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
