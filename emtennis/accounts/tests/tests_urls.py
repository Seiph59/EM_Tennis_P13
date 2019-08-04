""" Test file for urls.py file """

from django.test import TestCase
from django.urls import resolve
from accounts.views import create, account

class AccountTest(TestCase):
    """ Class for urls tests """

    def test_register_url_resolves_to_create_view(self):
        """ test if the url for register is associated
        with the create view """
        found = resolve('/register/')
        self.assertEqual(found.func, create)

    def test_my_account_url_resolves_to_account_view(self):
        """ test if the url for myaccount is associated
        with the account view """
        found = resolve('/myaccount/')
        self.assertEqual(found.func, account)