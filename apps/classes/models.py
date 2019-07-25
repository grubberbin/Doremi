from django.db import models


# Create your models here.


class ClassInfo(models.Model):
    CLASS_CHOICES = (
        ("xxb", "小小班"),
        ("xb", "小班"),
        ("zb", "中班"),
        ("db", "大班")
    )

    school_name = models.CharField(max_length=10, verbose_name='园区', null=False, default='')
    class_name = models.DateField(choices=CLASS_CHOICES, max_length=3, verbose_name='班级')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name
