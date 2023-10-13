from django.urls import path, include
from . import views
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, logout_user, login_user, edit_product, pantex, add_product_ajax, get_product_json, edit_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_product_by_one/<int:product_id>/', views.delete_product_by_one, name='delete_product_by_one'),
    path('add_product_by_one/<int:product_id>/', views.add_product_by_one, name='add_product_by_one'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('pantex/', pantex, name='pantex'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/', edit_product_ajax, name='edit_product_ajax'),
]