from django.db import models


# Create your models here.

class ContactInfo(models.Model):
    username = models.CharField(max_length=50, verbose_name='姓名', default='')
    mobile = models.CharField(max_length=11, null=False, blank=True, verbose_name='手机号')
    message = models.TextField(max_length=500, verbose_name='留言')

    class Meta:
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
