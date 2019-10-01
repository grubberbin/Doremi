from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
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

        return render(request, 'shop/details.html', {'goods': goods, 'others_list': others_list})


class CartInfoView(LoginRequiredMixin, View):

    def get(self, request):

        username = request.user
        user = UserProfile.objects.get(username=username)
        try:
            cart_list = Cart.objects.filter(u_id_id=user.id)
        except Cart.DoesNotExist:
            return

        return render(request, 'shop/cart.html', {'cart_list': cart_list})

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


class AddCartView(LoginRequiredMixin, View):

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

        user = UserProfile.objects.get(username=user.username)

        try:
            cart = Cart.objects.get(g_id_id=sku_id)
            number = int(cart.count)
            number += count
            cart.count = str(number)
            cart.save()
        except Cart.DoesNotExist:
            Cart.objects.create(g_id_id=sku_id, u_id_id=user.id, count=count)
            return JsonResponse({'res': 6, 'message': '商品已加入购物车'})

            # 返回应答
        return JsonResponse({'res': 6, 'message': '商品已加入购物车'})


class DeleteCartView(LoginRequiredMixin, View):

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        cart_id = request.POST.get('cart_id')

        # 数据校验
        if not cart_id:
            return JsonResponse({'res': 1, 'errmsg': '无效商品id'})

        # 业务处理：删除购物车
        Cart.objects.filter(id=cart_id).delete()

        # 返回应答
        return JsonResponse({'res': 2, 'message': '删除  成功'})


class UpdateCartView(LoginRequiredMixin, View):
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


class OrderInfoView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        username = request.user
        user = UserProfile.objects.get(username=username)
        cart_list = Cart.objects.filter(u_id=user)
        for cart in cart_list:
            cart.total = float(cart.g_id.price) * int(cart.count)

        return render(request, 'shop/order.html', {'goods_list': cart_list})

    @csrf_exempt
    def post(self, request):
        res = dict()
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        return render(request, 'shop/pageJump.html')
