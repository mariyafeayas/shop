from django.urls import path
from shop.views import *


urlpatterns = [
    path('', catalog),
    path('orders/', orders),
    path('create/<int:product_id>/', create_order, name="order_create"),
    path('product_detail/<int:product_id>/', product_detail, name = 'product_detail'),
    
]