from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic.base import View
from shop.models import Goods
from users.models import Teacher
from .models import Gallery, Feedback
# Create your views here.

from users.models import UserProfile


class IndexView(View):

    def get(self, request):
        # print(request.COOKIES.get('sessionid'))
        goods_list = Goods.objects.all()
        teachers = Teacher.objects.all()
        pictures = Gallery.objects.all()
        feedbacks = Feedback.objects.all()
        return render(request, 'index.html', {'pictures': pictures,
                                              'feedbacks': feedbacks,
                                              'teachers': teachers,
                                              'goods_list': goods_list})
