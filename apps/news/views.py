from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from .models import News

import logging

# Create your views here.

logger = logging.getLogger(__name__)


class NewsListView(View):

    def get(self, request):
        news_list = News.objects.all()
        for news in news_list:
            news.time = news.create_time.strftime("%Y - %M -%d %H:%m")

        return render(request, 'news/news.html', {'news_list': news_list})


class NewsInfoView(View):

    def get(self, request, news_id):
        news = News.objects.get(Q(id=news_id))
        news.time = news.create_time.strftime("%Y - %M -%d %H:%m")
        return render(request, 'news/news_details.html', {'news': news})
