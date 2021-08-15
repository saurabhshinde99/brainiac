from django.db import models
from django.utils import timezone as timez

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField(max_length=255)
    msg=models.CharField(max_length=255)
    date=models.DateField(default=timez.now,null=False)

    def __str__(self):
        return self.name