from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import Goods, Order, Cart
from django.views.decorators.csrf import csrf_exempt
import json


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


class CartView(View):

    def get(self, request):
        cart_list = Cart.objects.all()
        return render(request, 'shop/cart-page.html', {'cart_list': cart_list})

    @csrf_exempt
    def post(self, request):
        res = dict()
        # data = json.loads(request.bod)
        data = request.POST
        gid = data.get('gid', '')
        count = data.get('count', '')
        goods = Goods.objects.get(id=gid)
        if gid and count:
            cart = Cart()
            cart.u_id = request.user
            cart.g_id = goods
            cart.count = count
            cart.save()
            res['status'] = 'success'
        else:
            res['status'] = 'fail'
        return HttpResponse(json.dumps(res), content_type='application/json')


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
