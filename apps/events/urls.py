from django.urls import path
from django.views.generic import TemplateView
from .views import EventInfoView, EventDetailView

app_name = 'events'

urlpatterns = [
    # 活动信息
    path('', EventInfoView.as_view(), name='events'),
    path('<int:event_id>/', EventDetailView.as_view(), name='event_detial'),
]
