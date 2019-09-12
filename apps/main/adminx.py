# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 10:58
# @Author  : Griy
# @Email   : Griy26d@163.com
# @File    : adminx.py
# @Software : PyCharm

import xadmin
from xadmin import views
from .models import Gallery, Feedback


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '哆唻咪后台管理系统'
    site_footer = '哆唻咪启蒙乐园 2019-2099'
    menu_style = 'accordion'


class GalleryManager(object):
    list_display = ['title', 'create_time']
    search_fields = ['title']
    list_filter = []


class FeedbackManager(object):
    list_display = ['name', 'content', 'create_time']
    search_fields = ['name']
    list_filter = []


xadmin.site.register(Gallery, GalleryManager)
xadmin.site.register(Feedback, FeedbackManager)
