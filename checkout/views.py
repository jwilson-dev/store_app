from django.shortcuts import render

from cart.models import Cart
from products.models import Product

def proceed(request):
    cart, status = Cart.objects.get_or_create()
    total = sum([item.price for item in cart.items.all()])
    for c in cart.items.all():
        product = Product.objects.get(pk=c.pk)
        product.stock -= 1
        product.save()
    cart.delete()
    return render(request, 'pages/index.html')
