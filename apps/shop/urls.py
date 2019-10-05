from django.urls import path

from .views import ShopInfoView, AddCartView, ProductInfoView, OrderInfoView, CartInfoView, UpdateCartView, \
    DeleteCartView, page_jump

app_name = 'shop'

urlpatterns = [
    # 商城信息
    path('', ShopInfoView.as_view(), name='shop'),
    path('cart/', CartInfoView.as_view(), name='cart'),
    path('cart/add', AddCartView.as_view(), name='add_cart'),
    path('cart/delete', DeleteCartView.as_view(), name='delete_cart'),
    path('cart/update', UpdateCartView.as_view(), name='update_cart'),
    path('order/', OrderInfoView.as_view(), name='order'),
    path('goods/<int:goods_id>/', ProductInfoView.as_view(), name='good_details'),
    path('details/', ProductInfoView.as_view(), name='details'),
    path('jump/', page_jump)
]
