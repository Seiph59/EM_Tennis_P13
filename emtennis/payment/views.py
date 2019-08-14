from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse
from events.models import Registration
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

def process_payment(request):
    """Method to allow user to pay """
    order_id = request.session.get('order_id')
    registration = get_object_or_404(Registration, order_id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': registration.amount,
        'item_name': 'Inscription {}'.format(registration.event.title),
        'invoice': order_id,
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process_payment.html', {'registration': registration, 'form': form})

@csrf_exempt
def payment_done(request):
    """ Paypal return here if the payment is completed by user """
    order_id = request.session.get('order_id')
    registration = get_object_or_404(Registration, order_id=order_id)
    # registration.paid = True
    registration.save()
    return render(request, 'payment/payment_done.html')

@csrf_exempt
def payment_canceled(request):
    """Paypal return here if the payment is canceled by user"""
    return render(request, 'payment/payment_cancelled.html')