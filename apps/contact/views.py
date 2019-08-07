from django.shortcuts import render
from django.views.generic.base import View

from .forms import ContactForm
from .models import ContactInfo


# Create your views here.


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            username = request.POST.get('username', None)
            #print(username)
            phone = request.POST.get('phone', None)
            #print(phone)
            message = request.POST.get('message', None)
            #print(message)
            if username and phone and message:
                info = ContactInfo()
                info.username = username
                info.phone = phone
                info.message = message
                info.save()
                return render(request, 'contact.html', {'msg': '提交成功！'})
            else:
                return render(request, 'contact.html', {'msg': '数据错误'})
        else:
            return render(request, 'contact.html', {'msg': '手机号格式错误'})
