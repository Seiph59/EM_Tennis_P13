from django.shortcuts import render, redirect
from events.models import Event
from accounts.models import Profile
from events.forms import RegistrationForm

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
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            current_user = request.user
            profile = Profile.objects.get(user=current_user.id)
            profile.save()
            registration = registration_form.save(commit=False)
            registration.profile = profile
            registration.event = event
            registration.save()
            return redirect('events:index')

    else:
        registration_form = RegistrationForm()
        return render(request, 'events/event_page.html', {'event': event,
                                                        'registration_form': registration_form})
