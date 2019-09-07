from django.urls import path
from .views import NewsListView, NewsInfoView

app_name = 'news'

urlpatterns = [
    # 新闻信息
    path('', NewsListView.as_view(), name='news'),
    path('<int:news_id>/', NewsInfoView.as_view(), name='news_details'),
]
