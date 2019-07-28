from django.test import TestCase, Client
from django.urls import resolve, reverse
from events.views import index


class HomePageTest(TestCase):
    """ Class for homepage url test """

    def test_root_url_resolves_to_home_page_view(self):
        """ Test if welcome page works """
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_welcome_page_path(self):
        """ Test  which control if the template used
        is the good one, and path correctly assigned"""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/index.html')
