from django.urls import path
from .apps import UsersConfig
from .views import UserInfoView, LoginView, RegisterView, ForgetPwdView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name='user_info'),
]
