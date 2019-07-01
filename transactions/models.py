from django.db import models
import uuid

from products.models import Product 

class Transaction(models.Model):
    ref_code = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    items = models.ManyToManyField(Product)
    trans_date = models.DateTimeField(auto_now_add=True)