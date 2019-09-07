from django.db import models


# Create your models here.

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='标题', null=False, blank=False)
    subject = models.CharField(max_length=100, verbose_name='主题', null=False, blank=False)
    price = models.CharField(max_length=50, verbose_name='费用', null=False, blank=False)
    create_time = models.DateTimeField(null=False, blank=False, verbose_name='发布时间')
    start_time = models.DateTimeField(null=False, blank=False, verbose_name='开始时间')
    end_time = models.DateTimeField(null=False, blank=False, verbose_name='结束时间')
    content = models.TextField(null=False, blank=False, verbose_name='活动内容', default='活动内容:\r\n')
    attention = models.TextField(null=False, blank=False, verbose_name='注意事项', default='注意事项:\r\n')
    address = models.CharField(max_length=50, verbose_name='地点', null=False, blank=False)
    awards = models.CharField(max_length=50, verbose_name='奖项', null=False, blank=False)
    class_id = models.CharField(max_length=50, verbose_name='活动对象', null=False, blank=False)
    teachers = models.CharField(max_length=50, verbose_name='负责老师', null=False, blank=False)
    mobile = models.CharField(max_length=50, verbose_name='联系方式', null=False, blank=False)
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m/%d', default='image?default.png', verbose_name='封面图')

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
