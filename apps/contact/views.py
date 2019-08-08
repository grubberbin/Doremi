from django.shortcuts import render
from django.views.generic.base import View

from .forms import ContactForm
from .models import ContactInfo

import datetime


# Create your views here.


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            username = request.POST.get('username', None)
            phone = request.POST.get('phone', None)
            message = request.POST.get('message', None)
            if username and phone and message:
                info = ContactInfo()
                info.username = username
                info.mobile = phone
                info.message = message
                info.save()
                return render(request, 'contact.html', {'msg': '提交成功！'})
            else:
                return render(request, 'contact.html', {'msg': '数据错误'})
        else:
            return render(request, 'contact.html', {'msg': '手机号格式错误'})
