""" Payment models """

# Django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PaymentType(models.Model):
    """ Payment type model. """
    
    INSCRIPTION = 'INS'
    CROSSFIT = 'CRF'
    FUNCTIONAL = 'FUN'
    KICKBOXING = 'KBX'
    ALL_ACCESS = 'ALL'

    PAYMENT_CHOICES = (
        (INSCRIPTION, 'Inscription'),
        (CROSSFIT, 'Crossfit'),
        (FUNCTIONAL, 'Functional'),
        (KICKBOXING, 'Kickboxing'),
        (ALL_ACCESS, 'All access'),
    )

    payment_code = models.CharField(max_length=3, choices=PAYMENT_CHOICES)    
    amount = models.FloatField()

    def __str__(self):
        """ Return payment code and amount. """
        return f'{self.get_payment_code_display()} - Amount: {self.amount}'


class Payment(models.Model):
    """ Payment model. """

    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET("UNS"))
    date = models.DateField(default=timezone.now)
    reference = models.IntegerField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Return payment info such as type, athlete and date. """
        return f'{self.payment_type.__str__()}, date: {self.date}, '
        f'athlete: {self.athlete}'

    def get_absolute_url(self):
        """ Return payment url. """
        return reverse('payment-detail', kwargs={'pk': self.pk})
