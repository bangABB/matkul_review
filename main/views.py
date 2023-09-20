from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product  # Assuming your Product model is defined in 'main.models'
from django.db.models import Sum
from django.http import HttpResponse
from django.core import serializers


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_main(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    total_jumlah_mahasiswa = products.aggregate(total=Sum('jumlah_mahasiswa'))['total']

    user_data = {
        'nama_user': 'Masabil Arraya Muhammad',
        'kelas_user': 'PBP A',
        'NPM': "2206082101"
    }

    application_data = {
        'nama_aplikasi': 'REVIEW MATKUL',
        'tanggal_dibuat': '13/09/2023'
    }

    # Pass the products, user_data, and application_data to the template
    context = {
        'products': products,
        'user_data': user_data,
        'application_data': application_data,
        'total_jumlah_mahasiswa': total_jumlah_mahasiswa,
    }

    return render(request, "main.html", context)
