from django.db import models
from accounts.models import Profile


class Event(models.Model):
    """ Create Event model """
    title = models.CharField(max_length=250)
    image = models.ImageField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    adult_price = models.DecimalField(max_digits=5, decimal_places=2)
    child_price = models.DecimalField(max_digits=5, decimal_places=2)
    registered = models.ManyToManyField(Profile, through="Registration",
        through_fields=('event', 'profile')
    )

class Registration(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    adult_number = models.PositiveSmallIntegerField(default=0)
    child_number = models.PositiveSmallIntegerField(default=0)
    payment_date_time = models.DateTimeField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=250, null=True)
