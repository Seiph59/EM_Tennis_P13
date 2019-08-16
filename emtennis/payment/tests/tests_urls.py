
from django.test import TestCase
from django.urls import resolve
from payment import views

class PaymentTest(TestCase):
    """ Class for urls tests """

    def test_process_payment_url_resolves_to_payment_view(self):
        """ test if the url for process payment is associated
        with the payment view """
        found = resolve('/process-payment/')
        self.assertEqual(found.func, views.process_payment)

    def test_payment_done_url_resolves_to_payment_done_view(self):
        """ test if the url for payment_done is associated
        with the payment done view """
        found = resolve('/payment-done/')
        self.assertEqual(found.func, views.payment_done)

    def test_payment_canceled_url_resolves_to_payment_canceled_view(self):
        """ test if the url for payment canceled is associated
        with the payment canceled view """
        found = resolve('/payment-cancelled/')
        self.assertEqual(found.func, views.payment_canceled)