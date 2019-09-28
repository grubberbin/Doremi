from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from django.http import JsonResponse
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
                return HttpResponsePermanentRedirect(reverse('main:index'))
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

            user = UserProfile()
            user.username = user_name
            user.nick_name = user_name
            user.is_active = True
            user.password = make_password(pass_word)
            user.save()
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
        '''

        :param request:
        :return:
        '''
        return render(request, 'users/usercenter-info.html')

    # 用户修改昵称，手机号，地址，生日
    def post(self, request):
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if gender and email and phone and address:
            user = UserProfile.objects.get(username=request.user.username)

            user.gender = 'male' if (gender == '1') else 'female'
            user.mobile = phone
            user.address = address
            user.email = email
            user.save()
            res = 'success'
        else:
            res = 'fail'

        return JsonResponse({'status': res, 'message': '个人信息更新成功'})


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse('main:index'))


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
