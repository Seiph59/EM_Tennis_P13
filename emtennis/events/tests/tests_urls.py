from django.test import TestCase, Client
from django.urls import resolve, reverse
from events.views import index
from events.models import Event
import tempfile


class HomePageTest(TestCase):
    """ Class for homepage url test """

    def test_root_url_resolves_to_home_page_view(self):
        """ Test if welcome page works """
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_welcome_page_path(self):
        """ Test which control if the template used
        is the good one, and path correctly assigned"""
        client = Client()
        response = client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/index.html')

    def test_events_list_path(self):
        """Test which control if the patch used
        is well linked with the good template"""
        client = Client()
        response = client.get(reverse('events:events'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events_list.html')

    def test_event_detail_page_path(self):
        """Test to check if we can access to the event
        page details """
        client = Client()
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        first_event = Event(title="Event 1",
                            image=image,
                            description="description test",
                            event_date='2019-08-04 17:22:45.311774+02',
                            adult_price=10,
                            child_price=5)
        first_event.save()
        event = Event.objects.all().first()
        response = client.get('/event/%d/' % (event.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_page.html')