from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm, LoginForm
from .models import UserProfile


class LoginView(View):
    # 显示注册页面
    def get(self, request):
        # 把form传给前端,里边是验证码需要在前端显示
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'login.html', {'login_form': login_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            # 实例化一个user_profile对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = check_password(pass_word)
            user_profile.save()
            # send_register_eamil(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    # 显示注册页面
    def get(self, request):
        # 把form传给前端,里边是验证码需要在前端显示
        register_form = RegisterForm()
        return render(request, 'register.html', {'captcha_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'captcha_form': register_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            # 实例化一个user_profile对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            # send_register_eamil(user_name, 'register')
            return render(request, 'register.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


# 让用户可以用邮箱登录
# setting 里要有对应的配置
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 全局 404 处理函数
def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局 500 处理函数
def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
