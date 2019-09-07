from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from .models import Events


# Create your views here.


class EventInfoView(View):

    def get(self, request):
        events = Events.objects.all()
        event_list = []
        for ev in events:
            time_start = ev.start_time.strftime("%H:%M")
            time_end = ev.end_time.strftime("%H:%M")
            event_list.append(
                {
                    'id': ev.id,
                    'title': ev.title,
                    'address': ev.address,
                    'day': ev.end_time.strftime('%d'),
                    'month': ev.end_time.strftime("%b"),
                    'time': time_start + ' - ' + time_end,
                    'image': ev.image.url,
                }
            )
        else:
            msg = 'Not events!'
        return render(request, 'events/events.html', {'events': event_list, 'msg': msg})


class EventDetailView(View):

    def get(self, request, event_id):
        event = Events.objects.get(Q(id=event_id))
        event.time = event.start_time.strftime('%Y-%m-%d %H:%M')
        event.image_url = event.image.url
        return render(request, 'events/events-details.html', {'event': event})
