from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect, render_to_response
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from .forms import RegisterForm, LoginForm, ForgetForm, UserInfoForm
from .models import UserProfile
from utils.mixin_utils import LoginRequiredMixin

import json


# setting 里要有对应的配置
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                print(request.user.username)
                return HttpResponsePermanentRedirect(reverse('index'))
            return render(request, 'users/login.html', {'msg': '用户名或者密码错误！'})
        else:
            print('login data error')
            login_form = LoginForm()
            return render(request, 'users/login.html', {'login_form': login_form})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'users/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', None)
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'users/register.html', {'register_form': register_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            re_pass_word = request.POST.get('re-password', None)
            if pass_word != re_pass_word:
                return render(request, 'users/register.html', {'register_form': register_form, 'msg': '两次输入密码不一致'})

            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = True
            user_profile.password = make_password(pass_word)
            user_profile.save()
            return render(request, 'index.html')
        else:
            return render(request, 'users/register.html', {'register_form': register_form})


# 忘记密码页面
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'users/forgot.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            return render(request, 'send_success.html')
        return render(request, 'users/forgot.html', {'forget_form': forget_form})


# userprofile
class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/usercenter-info.html')

    # 用户修改昵称，手机号，地址，生日
    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        res = dict()

        if user_info_form.is_valid():
            user_info_form.save()
            res['status'] = 'success'

        else:
            res = user_info_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        print('logout', request)
        return HttpResponsePermanentRedirect(reverse('index'))


# 全局 404 处理函数
def page_not_found(request, exception):
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
