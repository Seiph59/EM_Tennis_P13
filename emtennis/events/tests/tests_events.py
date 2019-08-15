""" Test file about events, registrations,
and data inserted in database """

from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import Profile
from events.models import Event, Registration
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

        self.user = User.objects.create(username='seiph',
                                first_name='Jean',
                                last_name='Robert',
                                email='jbr@aol.com',
                                password='kevin1234')
        self.profile = Profile.objects.create(user=self.user)

    def test_if_event_is_well_created(self):
        """ Check if create an event is working """
        basic_event_status = Event.objects.count()
        self.assertEqual(basic_event_status, 1)

    def test_if_the_user_logged_can_register_to_an_event(self):
        """Integration test which check the registration
        functionnality to an event is working """
        event_id = self.event.pk
        self.client.force_login(self.user)
        self.client.post('/event/' + str(event_id) + '/', data={'adult_number': 1,
                                        'child_number':0,
                                        'registered': True})
        registration_accounts = Registration.objects.count()
        self.assertEqual(registration_accounts, 1)

