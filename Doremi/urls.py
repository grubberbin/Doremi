"""Doremi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

import xadmin
from users.views import LogoutView, LoginView, RegisterView, ForgetPwdView


schema_view = get_swagger_view(title='API文档')

urlpatterns = [
                  path('xadmin/', xadmin.site.urls),
                  path(r'docs/', schema_view),

                  # 验证码
                  path('captcha/', include('captcha.urls')),

                  # 主页
                  path('', include('main.urls', namespace='main')),

                  path('login/', LoginView.as_view(), name='login'),

                  path('register/', RegisterView.as_view(), name='register'),

                  path('forgot/', ForgetPwdView.as_view(), name='forgot'),

                  path('logout/', LogoutView.as_view(), name='logout'),

                  # 用户中心 URL 配置
                  path('user/', include('users.urls', namespace='users')),

                  # 商城
                  path('shop/', include('shop.urls', namespace='shop')),

                  # 活动
                  path('events/', include('events.urls', namespace='events')),

                  # 新闻
                  path('news/', include('news.urls', namespace='news')),

                  # 联系我们
                  path('contact/', include('contact.urls', namespace='contact')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 全局 404 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
