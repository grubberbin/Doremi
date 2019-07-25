from django.db import models


# Create your models here.


class ClassInfo(models.Model):
    CLASS_CHOICES = (
        ("xxb", "小小班"),
        ("xb", "小班"),
        ("zb", "中班"),
        ("db", "大班")
    )

    school_id = models.CharField(max_length=10, verbose_name='园区号', null=False, default='')
    school_name = models.CharField(max_length=10, verbose_name='园区名称', null=False, default='')
    class_name = models.DateField(choices=CLASS_CHOICES, max_length=3, verbose_name='班级')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    main_teacher = models.CharField(max_length=20, default='', verbose_name='班主任')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    child_number = models.IntegerField(null=False, default=0, verbose_name='班级人数')

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name
