from django.db import models


# Create your models here.

class News(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=50, verbose_name='标题', null=False, blank=False)
    content = models.TextField(max_length=1500, verbose_name='内容', null=False, blank=False)
    create_time = models.DateTimeField(null=False, blank=False, verbose_name='发布时间')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
