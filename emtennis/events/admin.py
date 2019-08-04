from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created_date', 'last_update')
    search_fields = ['title', 'event_date']

admin.site.register(Event, EventAdmin)
