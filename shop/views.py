from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Cart
from django.views import generic

class ProductsList(ListView):
    """Список всех товаров"""
    model = Product
    template_name = "shop/list-product.html"


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    context_object_name = "product"
    template_name = "shop/product-detail.html"


class CartView(ListView):
    """Корзина"""
    model = Cart
    context_object_name = "cart"
    template_name = "shop/cart.html"
