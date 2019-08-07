# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 16:28
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : forms.py
# @Software : PyCharm

from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.Textarea()
