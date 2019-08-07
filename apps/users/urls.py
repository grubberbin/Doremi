from django.urls import path
from .apps import UsersConfig
from .views import UserInfoView, LoginView, RegisterView, ForgetPwdView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name='user_info'),

    path('login/', LoginView.as_view(), name='login'),

    path('register/', RegisterView.as_view(), name='register'),

    path('forgot/', ForgetPwdView.as_view(), name='forgot'),

    path('logout/', LogoutView.as_view(), name='logout'),
]
