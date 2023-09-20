from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "kelas", "jumlah_mahasiswa", "deskripsi","nilai"]