from django.shortcuts import get_object_or_404
from events.models import Registration
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.utils import timezone


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        registration = get_object_or_404(Registration, id=ipn.invoice)

        if registration.amount == ipn.mc_gross:
            registration.paid = True
            registration.payment_date_time = timezone.now()
            registration.save()