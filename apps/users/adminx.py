# -*- coding: utf-8 -*-
# @Time    : 2019-07-25 11:06
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : adminx.py
# @Software : PyCharm

import xadmin
from xadmin import views
from .models import Teacher, ClassInfo, Child


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '哆唻咪后台管理系统'
    site_footer = '哆唻咪启蒙乐园 2019-2099'
    menu_style = 'accordion'


# ------


class TeachersManager(object):
    list_display = ['user_id', 'nick_name', 'birthday', 'gender', 'class_info', 'work_years', 'points', 'mobile']
    search_fields = ['user_id', 'class_info', 'work_years', 'mobile', 'email']
    list_filter = ['gender', 'work_years']


class ClassesManager(object):
    list_display = ['school_id', 'class_name', 'address', 'main_teacher', 'mobile', 'child_number']
    search_fields = ['school_id', 'class_name', 'main_teacher', 'mobile', 'mobile']
    list_filter = ['school_id', 'class_name', 'main_teacher']


class ChildrenManager(object):
    list_display = ['user_id', 'nick_name', 'birthday', 'gender', 'age', 'address', 'mobile']
    search_fields = ['user_id', 'nick_name', 'gender', 'age', 'mobile']
    list_filter = ['gender', 'age']


'''
 直接修改 xadmin 的源码，即 xadmin/plugins/auth.py 里添加这两行代码
from django.contrib.auth import get_user_model
User = get_user_model()
 就可以代替下面那段代码
'''

xadmin.site.register(Teacher, TeachersManager)
xadmin.site.register(ClassInfo, ClassesManager)
xadmin.site.register(Child, ChildrenManager)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
