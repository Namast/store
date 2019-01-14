from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products_all'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
]