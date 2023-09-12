from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    classes = models.CharField(max_length=1)
    description = models.TextField()
    amount = models.IntegerField()
    nilai = models.CharField(max_length=2)
