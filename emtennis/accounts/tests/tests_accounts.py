""" Test file about accounts creation,
and data into the database """

from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserAccountTest(TestCase):
    """ Test about User account, database, creation """

    def test_new_user_account_created(self):
        """ Check if the database, save the user """
        accounts_before = User.objects.count()
        self.assertEqual(accounts_before, 0)
        User.objects.create_user(username="test",
                                 first_name="Al",
                                 last_name="taga",
                                 email="albg@sfr.fr",
                                 password="kevin1234")
        accounts_after = User.objects.count()
        self.assertEqual(accounts_after, 1)

    def test_no_account_db(self):
        """ Check if no account in the database """
        count_accounts = User.objects.count()
        self.assertEqual(count_accounts, 0)


    def test_account_created_by_client(self):
        """ Check if create an account from Client is working """
        basic_account_status = User.objects.count()
        self.assertEqual(basic_account_status, 0)
        client = Client()
        client.post('/register/', {'username': 'seiph2',
                                   'first_name': 'Damien',
                                   'last_name': 'Galasso',
                                   'email': 'damien@seiph.com',
                                   'password1': 'Openclassrooms',
                                   'password2': 'Openclassrooms'})
        account_count = User.objects.count()
        self.assertEqual(account_count, 1)
