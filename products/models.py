from django.db import models
from categories.models import Category
from datetime import datetime

class Product(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    stock =  models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=1)
    add_date = models.DateTimeField(default = datetime.now)
    last_restock = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
