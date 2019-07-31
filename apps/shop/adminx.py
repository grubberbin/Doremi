import xadmin
from xadmin import views


# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '哆唻咪后台管理系统'
    site_footer = '哆唻咪启蒙乐园 2019-2099'
    menu_style = 'accordion'


# ------

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
