from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
    
# class PaymentDescription(models.Model):
#     INSCRIPTION = 'INS'
#     JANUARY = 'JAN'
#     FEBRUARY = 'FEB'
#     MARCH = 'MAR'
#     APRIL = 'APR'
#     MAY = 'MAY'
#     JUNE = 'JUN'
#     JULY = 'JUL'
#     AUGUST = 'AUG'
#     SEPTEMBER = 'SEP'
#     OCTOBER = 'OCT'
#     NOVEMBER = 'NOV'
#     DECEMBER = 'DEC'

#     NAME_CHOICES = [
#         ('Months', (
#             (JANUARY, 'January'),
#             (FEBRUARY, 'February'),
#             (MARCH, 'March'),
#             (APRIL, 'April'),
#             (MAY, 'May'),
#             (JUNE, 'June'),
#             (JULY, 'July'),
#             (AUGUST, 'August'),
#             (SEPTEMBER, 'September'),
#             (OCTOBER, 'October'),
#             (NOVEMBER, 'November'),
#             (DECEMBER, 'December')
#             )
#         )
#         ('Others', (
#             (INSCRIPTION, 'Inscription'),
#             )
#         )
#     ]
#     payment_name = models.CharField(max_length=3, choices=NAME_CHOICES)
#     amount = models.FloatField()

    #def __str__(self):
        #return NAME_CHOICES[self.payment_name]  

class PaymentType(models.Model):
    
    INSCRIPTION = 'INS'
    CROSSFIT = 'CRF'
    FUNCTIONAL = 'FUN'
    KICKBOXING = 'KBX'
    ALL_ACCESS = 'ALL'
    UNSPECIFIED = 'UNS'

    PAYMENT_CHOICES = (
        (INSCRIPTION, 'Inscription'),
        (CROSSFIT, 'Crossfit'),
        (FUNCTIONAL, 'Functional'),
        (KICKBOXING, 'Kickboxing'),
        (ALL_ACCESS, 'All access'),
        (UNSPECIFIED, 'Unspecified')
    )


    payment_code = models.CharField(max_length=3, choices=PAYMENT_CHOICES, default=UNSPECIFIED)    
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
