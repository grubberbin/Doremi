from django.urls import path

from .views import ShopInfoView, CartPageView, ProductInfoView, CheckoutPageView

app_name = 'shop'

urlpatterns = [
    # 商城信息
    path('', ShopInfoView.as_view(), name='shop'),
    path('info/', ShopInfoView.as_view(), name='shop_info'),
    path('cart-page/', CartPageView.as_view(), name='cart-page'),
    path('checkout-page/', CheckoutPageView.as_view(), name='checkout-page'),
    path('product-details/', ProductInfoView.as_view(), name='product-details'),
]
