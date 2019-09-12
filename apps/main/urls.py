# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 11:07
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : urls.py
# @Software : PyCharm

from django.urls import path
from .views import IndexView, AboutView

app_name = 'main'

urlpatterns = [
    # 新闻信息
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')
]
