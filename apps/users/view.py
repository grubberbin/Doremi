from django.views.generic.base import View
from .forms import RegisterForm
from django.shortcuts import render, HttpResponse


class RegisterView(View):
    # 显示注册页面
    def get(self, request):
        # 把form传给前端,里边是验证码需要在前端显示
        register_form = RegisterForm()
        return render(request, 'login.html', {'register_form': register_form})
