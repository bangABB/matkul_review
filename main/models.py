from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    kelas = models.CharField(max_length=1)
    deskripsi = models.TextField()
    jumlah_mahasiswa = models.IntegerField()
    nilai = models.CharField(max_length=2)