from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import News

import logging

# Create your views here.

logger = logging.getLogger(__name__)


class NewsListView(View):

    def get(self, request):
        news_list = News.objects.all().order_by('-create_time')

        # 获取分页器对象
        paginator = Paginator(news_list, 8)

        current_page = int(request.GET.get("page", 1))

        page = paginator.page(current_page)

        # 构建page_range
        max_page_count = 11
        max_page_count_half = int(max_page_count / 2)
        # 判断页数是否大于max_page_count
        if paginator.num_pages >= max_page_count:
            # 得出start位置
            if current_page <= max_page_count_half:
                page_start = 1
                page_end = max_page_count + 1
            else:
                if current_page + max_page_count_half + 1 > paginator.num_pages:
                    page_start = paginator.num_pages - max_page_count
                    page_end = paginator.num_pages + 1
                else:
                    page_start = current_page - max_page_count_half
                    page_end = current_page + max_page_count_half + 1
            page_range = range(page_start, page_end)
        else:
            page_range = paginator.page_range

        for news in page.object_list:
            news.time = news.create_time.strftime("%Y - %m -%d %H:%M")

        return render(request, 'news/news.html', locals())


class NewsInfoView(View):

    def get(self, request, news_id):
        news = News.objects.get(Q(id=news_id))
        news.time = news.create_time.strftime("%Y - %m -%d %H:%M")
        return render(request, 'news/news_details.html', {'news': news})
