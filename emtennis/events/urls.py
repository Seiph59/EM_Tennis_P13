from django.urls import path

from events import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events_list, name='events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('legalnotice/', views.legal, name="legalnotice"),
    path('contact/', views.contact, name="contact"),
]