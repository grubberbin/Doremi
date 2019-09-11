from django.db import models
from datetime import datetime
from users.models import UserProfile


# Create your models here.


class Goods(models.Model):
    id = models.AutoField(verbose_name='商品id', primary_key=True)
    name = models.CharField(null=False, blank=False, verbose_name='名称', max_length=10)
    color = models.CharField(null=False, blank=False, verbose_name='颜色', max_length=10)
    price = models.CharField(null=False, blank=False, verbose_name='价格', max_length=10)
    pic = models.ImageField(max_length=100, upload_to='goods/%Y/%m/%d', default='image/default.png', verbose_name='图片')
    description = models.TextField(null=False, blank=True, verbose_name='描述')
    type = models.CharField(null=False, blank=False, verbose_name='商品类型', max_length=20)
    number = models.IntegerField(null=False, blank=False, verbose_name='商品数量')
    tell_you = models.TextField(null=True, blank=True, verbose_name='商品须知')
    buyers_number = models.IntegerField(null=False, blank=False, verbose_name='购买人数', default=0)
    level = models.FloatField(null=False, blank=False, verbose_name='推荐指数', default=0.0)
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    u_id = models.ForeignKey(to=UserProfile, verbose_name='用户id', null=False, on_delete=models.DO_NOTHING)
    g_id = models.ForeignKey(to="Goods", to_field="id", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


class Order(models.Model):
    Order_STATUS_CHOICES = (
        (0, "已提交"),
        (1, "未支付"),
        (2, "已支付"),
        (3, "已完成"),
        (4, "已删除"),
        (5, "已失效"),
        (6, '待发货'),
        (7, '已发货'),
        (8, '待收货')
    )
    PAY_METHOD_CHOICES = (
        (1, "货到付款"),
        (2, "支付宝"),
    )
    id = models.CharField(verbose_name='订单id', primary_key=True, max_length=30, )
    g_id = models.ForeignKey(to="Goods", to_field="id", on_delete=models.DO_NOTHING)
    u_id = models.ForeignKey(to=UserProfile, verbose_name='用户id', null=False, on_delete=models.DO_NOTHING)
    type = models.CharField(choices=Order_STATUS_CHOICES, verbose_name='订单状态', max_length=5)
    address = models.CharField(max_length=100, verbose_name='收货地址', null=False, blank=False)
    count = models.IntegerField(blank=False, null=False, verbose_name='商品数量', default=1)
    pay_method = models.CharField(choices=PAY_METHOD_CHOICES, verbose_name='付款方式', max_length=10)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
