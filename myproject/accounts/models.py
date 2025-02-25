from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name