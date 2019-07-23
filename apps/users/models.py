from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    user_id = models.CharField(max_length=20,verbose_name='学号',null=False)
    nick_name = models.CharField(max_length=10, verbose_name='姓名', default='')
    birthday = models.DateField(null=False, blank=True, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image?default.png', verbose_name='头像')

    class Meta:
        verbose_name = '小朋友信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
