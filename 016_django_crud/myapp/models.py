from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")


    
# class Dept(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Emp(models.Model):
#     dept =models.ForeignKey(Dept,on_delete=models.SET_NULL,null=True)
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=50)
