from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class EventInfoView(View):

    def get(self, request):
        return render(request, 'events/events.html')


class EventDetailView(View):

    def get(self, request):
        return render(request, 'events/events-details.html')
