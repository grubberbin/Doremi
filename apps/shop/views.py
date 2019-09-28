from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import Goods, Order, Cart
from users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from utils.mixin_utils import LoginRequiredMixin
import json


# Create your views here.


class ShopInfoView(LoginRequiredMixin, View):

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


class CartInfoView(LoginRequiredMixin, View):

    def get(self, request):

        username = request.user
        user = UserProfile.objects.get(username=username)
        cart_list = Cart.objects.filter(u_id=user)
        for cart in cart_list:
            cart.total = float(cart.g_id.price) * int(cart.count)

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


class updateCartView(View):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 数据校验
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

        # 校验添加的商品数：
        try:
            count = int(count)
        except Exception as e:
            # 数目出错
            return JsonResponse({'res': 2, 'errmsg': '商品数目出错'})

        # 校验商品是否存在：
        try:
            sku = Goods.objects.get(id=sku_id)
        except Goods.DoesNotExist:
            # 商品不存在
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

        # 校验商品库存
        if count > sku.stock:
            return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})

        # 业务处理：更新购物车
        Cart.objects.filter(g_id=sku).update(count=count)

        # 返回应答
        return JsonResponse({'res': 5, 'message': '更新成功'})


class CheckoutPageView(View):

    def get(self, request):
        return render(request, 'shop/checkout-page.html')
