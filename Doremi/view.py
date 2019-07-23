# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 10:33
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : view.py.py
# @Software : PyCharm


from django.http import HttpResponse

def index(request):
    return HttpResponse('Wecome Doremi!')