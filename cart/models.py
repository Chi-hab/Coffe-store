from django.db import models
from shop.models import Products
# Create your models here.

class Order(models.Model):
    table_num = models.IntegerField(null=False , blank=False)
    created_at  =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.table_num)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"