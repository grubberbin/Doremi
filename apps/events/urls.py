from django.urls import path

from .views import EventInfoView, EventDetailView

app_name = 'events'

urlpatterns = [
    # 商城信息
    path('', EventInfoView.as_view(), name='events'),
    path('detial/', EventDetailView.as_view(), name='event_detial'),
]