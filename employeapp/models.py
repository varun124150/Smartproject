from django.db import models

# Create your models here.

class Employee(models.Model):
    name= models.CharField(max_length=200, null=False)
    phone =models.PositiveIntegerField(null=True)
    department=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,default='name@default.com')
    picture=models.ImageField(upload_to ='images/')
    address= models.CharField(max_length=200, null=False)
    def _str_(self):
        return self.name

