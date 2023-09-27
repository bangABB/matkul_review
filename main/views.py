from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product  # Assuming your Product model is defined in 'main.models'
from django.db.models import Sum
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


def delete_product_by_one(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete_product_by_one()
        return HttpResponseRedirect(reverse('main:show_main'))
    except Product.DoesNotExist:
        # Handle the case where the product with the given ID does not exist.
        return HttpResponse('Product not found', status=404)
    
def delete_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if product.user == request.user:  # Ensure the user can only delete their own products
            product.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            return HttpResponse('Unauthorized', status=401)  # User is not authorized to delete this product
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

@login_required(login_url='/login')
def show_main(request):
    # Retrieve all products from the database
    last_login = request.COOKIES.get('last_login', 'Cookie not found')  # Get the cookie or provide a default value
    products = Product.objects.filter(user=request.user)
    total_jumlah_mahasiswa = products.aggregate(total=Sum('jumlah_mahasiswa'))['total']
    user_data = {
        'user': request.user.username,
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
        'last_login': last_login,
    }

    return render(request, "main.html", context)
