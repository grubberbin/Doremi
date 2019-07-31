from django.urls import path
from .views import NesInfoView

app_name = 'news'

urlpatterns = [
    # 新闻信息
    path('', NesInfoView.as_view(), name='news'),
]
