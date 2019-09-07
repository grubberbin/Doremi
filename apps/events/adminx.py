import xadmin
from xadmin import views
from .models import Events


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '哆唻咪后台管理系统'
    site_footer = '哆唻咪启蒙乐园 2019-2099'
    menu_style = 'accordion'


class EventsManager(object):
    list_display = ['id', 'title', 'content', 'address', 'start_time']
    search_fields = ['title']
    list_filter = []


xadmin.site.register(Events, EventsManager)
