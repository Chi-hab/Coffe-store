from django.shortcuts import render,redirect , get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Products
from .cart import Cart
from .forms import *
from .models import *

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products,  id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product , quantity=cd['quantity'] , override_quantity=['override'])
        return redirect('cart_detail')
   
@require_POST
def cart_remove(request , product_id) :
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id )
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart':cart
    }
    return render(request , 'cart_detail.html' , context)


def order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()
            return redirect("order_details", order_id=order.id)
    else:
        form = OrderForm()
    return render(request , 'order.html' , {'form':form})


def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)   
    total_price = sum(item.price * item.quantity for item in order.items.all())
    return render(request, "order_details.html", {"order": order, "total_price": total_price})