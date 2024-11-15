from django.shortcuts import render
from .models import Product
from .models import Order


def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})


def orders(request):
    return render(request, 'shop/orders.html')


def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        u_address = request.POST["address"]
        u_phone = request.POST["phone"]
        u_comment = request.POST["comment"]
        u_count = request.POST["count"]
        Order.objects.create(
            product = product,
            address = u_address,
            phone = u_phone,
            comment = u_comment,
            count = u_count
        )
    return render(request, 'shop/create_order.html')
    

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product })

def orders(request):
    order = Order.objects.all()
    return render(request, 'shop/orders.html', {'orders': order })