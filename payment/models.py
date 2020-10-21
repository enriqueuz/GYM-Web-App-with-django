from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PaymentType(models.Model):
    
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
        return self.get_payment_code_display()

class Payment(models.Model):

    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET("UNS"))
    date = models.DateField(default=timezone.now)
    reference = models.IntegerField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_type.__str__()

    def get_absolute_url(self):
        return reverse('payment-detail', kwargs={'pk': self.pk})
