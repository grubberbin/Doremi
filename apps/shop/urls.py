from django.urls import path

from .views import ShopInfoView, CartPageView, ProductInfoView, CheckoutPageView

app_name = 'shop'

urlpatterns = [
    # 商城信息
    path('', ShopInfoView.as_view(), name='shop'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('order/', CheckoutPageView.as_view(), name='order'),
    path('<int:id>/', ProductInfoView.as_view(), name='details'),
    path('details/', ProductInfoView.as_view(), name='details'),
]
