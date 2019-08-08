from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.


class NesInfoView(View):

    def get(self, request):
        return render(request, 'news/news.html')
