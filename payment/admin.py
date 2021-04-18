""" Payment admin. """

# Django
from django.contrib import admin

# Models
from .models import Payment, PaymentType

admin.site.register(PaymentType)
admin.site.register(Payment)

