from django.shortcuts import render
from .models import Products
from cart.forms import CartAddProductForm
# Create your views here.

def home(request):
    latest_product = Products.objects.order_by('-created_at')[:3]
    cart_product_form = CartAddProductForm()
    context = {
        'latest_product':latest_product,
        'cart_product_form':cart_product_form ,
    }
    return render(request,'pages/home.html',context )

def menu(request):
    products = Products.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'cart_product_form':cart_product_form ,
        'products':products,
    }
    return render(request, 'pages/menu.html' , context)

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    pro = Products.objects.all()
    if 'searchname' in request.GET:
        name= request.GET['searchname']
        if name :
            pro=pro.filter(name__icontains=name)
        cart_product_form = CartAddProductForm()
        
    return render(request, 'pages/search.html', {'pro':pro , 'cart_product_form':cart_product_form})

