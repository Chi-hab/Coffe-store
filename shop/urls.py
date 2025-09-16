from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home , name='home'),
    path('menu/', views.menu , name='menu'),
    path('about/', views.about , name='about'),
    path('search/', views.search , name='search'),
]
