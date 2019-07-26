"""Doremi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import xadmin
from . import view
from django.views.generic import TemplateView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('events/', TemplateView.as_view(template_name='events.html'), name='events'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('events-detrails/', TemplateView.as_view(template_name='events-detrails.html'), name='events-detrails'),
    path('cart-page/', TemplateView.as_view(template_name='cart-page.html'), name='cart-page'),
    path('checkout-page/', TemplateView.as_view(template_name='checkout-page.html'), name='checkout-page'),
    path('product-details/', TemplateView.as_view(template_name='product-details.html'), name='product-details'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
