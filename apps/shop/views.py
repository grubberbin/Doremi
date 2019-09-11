from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from .models import Goods, Order


# Create your views here.


class ShopInfoView(View):

    def get(self, request):
        goods_list = Goods.objects.all()
        for goods in goods_list:
            goods.image_url = goods.pic.url
        return render(request, 'shop/shop.html', {'goods_list': goods_list})


class ProductInfoView(View):

    def get(self, request, goods_id):
        goods = Goods.objects.get(Q(id=goods_id))
        others_list = Goods.objects.filter(Q(type=goods.type) & ~Q(id=goods.id))

        return render(request, 'shop/product-details.html', {'goods': goods, 'others_list': others_list})


class AddCartView(View):

    def get(self, request, goods_id, quantity):
        goods = Goods.objects.get(Q(id=goods_id))
        goods.quantity = quantity
        goods.total = quantity * goods.price
        goods_list = [goods, ]

        if not goods_list:
            msg = '购物车没有宝贝哦，快去添加吧！'
        else:
            msg = '欢迎购物！'
        return render(request, 'shop/cart-page.html', {'goods_list': goods_list, 'msg': msg})


class CheckoutPageView(View):

    def get(self, request):
        return render(request, 'shop/checkout-page.html')
