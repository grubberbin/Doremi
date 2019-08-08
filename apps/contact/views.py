from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .forms import ContactForm
from .models import ContactInfo

import json


# Create your views here.


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        contact_form = ContactForm(request.POST)
        res = dict()
        if contact_form.is_valid():
            username = request.POST.get('username', None)
            phone = request.POST.get('phone', None)
            message = request.POST.get('message', None)
            info = ContactInfo()
            info.username = username
            info.mobile = phone
            info.message = message
            info.save()
            res['status'] = 'success'
            res['msg'] = '留言提交成功！'
        else:
            res['status'] = 'fail'
            res['msg'] = '格式错误'
        return HttpResponse(json.dumps(res), content_type='application/json')
