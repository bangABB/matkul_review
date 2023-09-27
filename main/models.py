from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    kelas = models.CharField(max_length=1)
    deskripsi = models.TextField()
    jumlah_mahasiswa = models.IntegerField()
    nilai = models.CharField(max_length=2)

    def delete_product_by_one(self):
        """
        Reduces the 'jumlah_mahasiswa' variable by one.
        """
        if self.jumlah_mahasiswa > 0:
            self.jumlah_mahasiswa -= 1
            self.save()

    @classmethod
    def delete_product(cls, product_id):
        """
        Deletes a specific product by its ID.
        """
        try:
            product = cls.objects.get(pk=product_id)
            product.delete()
            return True  # Deletion successful
        except cls.DoesNotExist:
            return False  # Product with the given ID does not exist

