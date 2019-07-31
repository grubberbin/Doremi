from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class ShopInfoView(View):

    def get(self, request):
        return render(request, 'shop/shop.html')


class ProductInfoView(View):

    def get(self, request):
        return render(request, 'shop/product-details.html')


class CartPageView(View):

    def get(self, request):
        return render(request, 'shop/cart-page.html')


class CheckoutPageView(View):

    def get(self, request):
        return render(request, 'shop/checkout-page.html')
