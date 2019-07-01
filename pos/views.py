from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from products.models import Product
from cart.models import Cart


def pos(request):
    products = Product.objects.all()
    context = {
        'products':products
    }

    return render(request, 'pages/index.html', context)

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(Q(code__icontains=query) | Q(name__icontains=query))
    context = {
        'products':results
    }
    return render(request, 'pages/index.html', context)

def add_to_cart(request, products_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=products_id)
    cart, status = Cart.objects.get_or_create()
    cart.items.add(product)
    cart.save()
    total = sum([item.price for item in cart.items.all()])
    context = {
        'products':products,
        'cart' : cart.items.all(),
        'total' : total
    }

    return render(request, 'pages/index.html', context)


def checkout(request):
    cart, status = Cart.objects.get_or_create()
    total = sum([item.price for item in cart.items.all()])
    context = {
        'total': total,
    }
    
    return render(request, 'pages/checkout.html', context)