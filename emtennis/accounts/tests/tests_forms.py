""" Test file for form's tests """
from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm


class FormsTest(TestCase):
    """ Class to do the form's tests """

    def setUp(self):
        """ Parameter for each test """
        self.data = {'username': 'seiph',
                     'first_name': 'Jean',
                     'last_name': 'Robert',
                     'email': 'jbr@aol.com',
                     'password1': 'kevin1234',
                     'password2': 'kevin1234'}

    def test_valid_form_true(self):
        """ test if form is valid """
        form = UserRegisterForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_valid_form_false(self):
        """ test if form is not valid """
        form = UserRegisterForm(data={'username': 'seiph'})
        self.assertFalse(form.is_valid())

    def test_error_user_already_exists(self):
        """ test if an error is raised bescause user's already exists """
        User.objects.create_user(self.data)
        client = Client()
        client.post('/register/', self.data)
        self.assertRaisesMessage(ValueError, 'user already exists')
