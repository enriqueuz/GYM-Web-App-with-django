from django.contrib import admin
from .models import Payment, PaymentType
# Register your models here.

admin.site.register(PaymentType)
admin.site.register(Payment)

