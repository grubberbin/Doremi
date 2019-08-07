# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 10:33
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : view.py.py
# @Software : PyCharm


from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.

from users.models import UserProfile


class IndexView(View):

    def get(self, request):
        ck = request.session.get("username")
        print(ck)
        return render(request, 'index.html')
