# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 16:22
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : urls.py
# @Software : PyCharm


from django.urls import path
from .apps import ContactConfig
from .views import ContactView

app_name = 'contact'

urlpatterns = [
    # 留言信息
    path('', ContactView.as_view(), name='contact'),
]
