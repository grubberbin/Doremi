from django.db import models

from datetime import datetime


# Create your models here.

class ContactInfo(models.Model):
    username = models.CharField(max_length=50, verbose_name='姓名', null=False, default='')
    mobile = models.CharField(max_length=11, null=False, verbose_name='手机号')
    message = models.TextField(max_length=500, null=False, verbose_name='留言')
    time = models.DateTimeField(default=datetime.now, verbose_name='时间', null=False)

    class Meta:
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
