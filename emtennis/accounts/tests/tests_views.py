""" Test file dedicated to test views """
from django.test import TestCase
from django.contrib.auth.models import User


class RedirectTest(TestCase):
    """ Class which is used to test if pages redirections work """

    def setUp(self):
        """ Parameter for each test """
        self.data = {'username': 'seiph',
                     'first_name': 'Jean',
                     'last_name': 'Robert',
                     'email': 'jbr@aol.com',
                     'password1': 'kevin1234',
                     'password2': 'kevin1234'}


    def test_redirect_if__try_access_myaccount_without_login(self):
        """ test redirection if user try to access the
        'my_account' page without login """
        response = self.client.get('/myaccount/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_when_account_created_to_homepage(self):
        """ test redirection when the user create his account """
        response = self.client.post('/register/', self.data)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('events/index.html')

    def test_redirect_when_login_to_homepage(self):
        """ test that the use is redirected when he logs in """
        User.objects.create_user(self.data)
        response = self.client.post('/login/', {'username': 'seiph',
                                                'password': 'kevin1234'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('events/index.html')

