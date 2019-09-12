from django.db import models
from datetime import datetime


# Create your models here.

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='说明', null=False, blank=False)
    image = models.ImageField(max_length=100, upload_to='main/image/%Y/%m', default='image?default.png',
                              verbose_name='图片')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='姓名', null=False, default='')
    content = models.TextField(max_length=200, verbose_name='反馈', null=False, blank=False, default='')
    image = models.ImageField(max_length=100, upload_to='main/image/%Y/%m', default='image?default.png',
                              verbose_name='头像')
    level = models.IntegerField(default=0, verbose_name='评价', null=False)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = '家长反馈'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
