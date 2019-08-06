from django.shortcuts import render
from events.models import Event

def index(request):
    """Root view, which will be display, when the user
    will try to access to the website. Events are display on this page"""
    event = Event.objects.order_by('event_date').all().first()
    return render(request, 'events/index.html', {'event': event})

def events_list(request):
    """ View which display all the events planned """
    events_list = Event.objects.order_by('event_date').all()
    return render(request, 'events/events_list.html', {'event_list': events_list})

def event_detail(request, event_id):
    """ Method for event_detail and to allow
    user to register """
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/event_page.html', {'event': event})