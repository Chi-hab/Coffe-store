from django.urls import path
from . import views


urlpatterns = [
    path('cart_add/<int:product_id>/', views.cart_add , name='cart_add'),
    path('cart_remove/<int:product_id>/', views.cart_remove , name='cart_remove'),
    path('cart_detail/', views.cart_detail , name='cart_detail'),
    path('order/', views.order , name='order'),
    path('order_details/<int:order_id>/', views.order_details , name='order_details'),
]