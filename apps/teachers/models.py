from django.db import models


# Create your models here.


class Teacher(models.Model):
    user_id = models.CharField(max_length=20, verbose_name='工号', null=False)
    nick_name = models.CharField(max_length=10, verbose_name='姓名', default='')
    birthday = models.DateField(null=True, blank=True, verbose_name='年龄')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    class_info = models.CharField(max_length=15, default='', verbose_name='班级')
    position = models.CharField(max_length=20, default='', verbose_name='职务')
    work_years = models.IntegerField('工作年限', default=0)
    points = models.CharField(verbose_name='教学特点', default='', max_length=50)
    mobile = models.CharField(max_length=11, null=False, blank=True, verbose_name='手机号')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id
