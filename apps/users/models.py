from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image?default.png', verbose_name='头像')

    class Meta:
        verbose_name = '普通用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class Teacher(models.Model):
    user_id = models.CharField(max_length=20, verbose_name='工号', null=False)
    name = models.CharField(max_length=10, verbose_name='姓名', default='')
    nick_name = models.CharField(max_length=10, verbose_name='昵称', default='')
    age = models.IntegerField(verbose_name='年龄', null=False, default=0)
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    class_info = models.CharField(max_length=15, default='', verbose_name='班级')
    position = models.CharField(max_length=20, default='', verbose_name='职务')
    work_years = models.IntegerField('工作年限', default=0)
    points = models.CharField(verbose_name='教学特点', default='', null=False, max_length=50)
    mobile = models.CharField(max_length=11, null=False, blank=False, verbose_name='手机号')
    email = models.CharField(max_length=50, null=False, blank=True, verbose_name='邮箱')
    image = models.ImageField(max_length=100, upload_to='teachers/%Y/%m', default='image?default.png',
                              verbose_name='头像')

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id


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
    mobile = models.CharField(max_length=11, null=False, blank=False, verbose_name='手机号')
    child_number = models.IntegerField(null=False, default=0, verbose_name='班级人数')

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name


class Child(models.Model):
    user_id = models.CharField(max_length=20, verbose_name='学号', null=False)
    nick_name = models.CharField(max_length=10, verbose_name='姓名', default='')
    birthday = models.DateField(null=False, blank=False, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    age = models.IntegerField(null=False, default=0, verbose_name='年龄')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=False, blank=False, verbose_name='手机号')
    image = models.ImageField(max_length=100, upload_to='children/%Y/%m', default='image?default.png',
                              verbose_name='头像')

    class Meta:
        verbose_name = '幼儿信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id
