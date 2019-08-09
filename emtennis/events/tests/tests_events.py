""" Test file about events, registrations,
and data inserted in database """

from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import Profile
from events.models import Event
import tempfile

class RegistrationTest(TestCase):
    """ Class to check if user is able
    to register for an event """
    def setUp(self):
        """ Parameters for each test """
        self.client = Client()
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.event = Event.objects.create(title="Test",
                                     image=image,
                                     description='description test',
                                     event_date='2019-08-04 17:22:45.311774+02',
                                     adult_price=10,
                                     child_price=5)

    def test_if_event_is_well_created(self):
        """ Check if create an event is working """
        basic_event_status = Event.objects.count()
        self.assertEqual(basic_event_status, 1)

