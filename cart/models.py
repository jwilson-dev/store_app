from django.db import models
from products.models import Product

class Cart(models.Model):
    ref_code = models.CharField(max_length=5)
    items = models.ManyToManyField(Product)
    is_order = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    last_transaction = models.DateTimeField(auto_now=True)