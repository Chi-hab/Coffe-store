from django.contrib import admin
from .models import *
# Register your models here.



class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table_num", "created_at")  # يظهر رقم الطاولة وتاريخ الطلب


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "price", "quantity")

admin.site.register(Order ,OrderAdmin)
admin.site.register(OrderItem , OrderItemAdmin)