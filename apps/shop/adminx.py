import xadmin
from xadmin import views
from .models import Goods, Order, Cart


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '哆唻咪后台管理系统'
    site_footer = '哆唻咪启蒙乐园 2019-2099'
    menu_style = 'accordion'


# ------

class GoodsManager(object):
    list_display = ['name', 'price', 'color', 'unit', 'stock']
    search_fields = ['name']
    list_filter = ['price', 'stock']


class OrdersManager(object):
    list_display = ['id', 'g_id', 'u_id', 'type', 'count', 'pay_method']
    search_fields = ['id', 'g_id', 'u_id']
    list_filter = ['type', 'pay_method']


class CartManager(object):
    list_display = ['id', 'g_id', 'u_id', 'count']
    search_fields = ['id', 'g_id', 'u_id']
    list_filter = ['g_id', 'u_id']


xadmin.site.register(Goods, GoodsManager)
xadmin.site.register(Order, OrdersManager)
xadmin.site.register(Cart, CartManager)
