from django.shortcuts import render, redirect

from cart.models import Cart
from products.models import Product
from transactions.models import Transaction

def proceed(request):
    transaction = Transaction.objects.create()
    cart, status = Cart.objects.get_or_create()
    total = sum([item.price for item in cart.items.all()])
    for c in cart.items.all():
        product = Product.objects.get(pk=c.pk)
        transaction.items.add(product)
        product.stock -= 1
        product.save()
    transaction.save()
    cart.delete()
    return redirect('index')
