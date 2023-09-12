from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    classes = models.CharField(max_length=1)
    jumlah = models.IntegerField()
    description = models.TextField()
    deskripsi = models.TextField()
    difficulty = models.TextField()
    nilai = models.TextField(max_length=2)
