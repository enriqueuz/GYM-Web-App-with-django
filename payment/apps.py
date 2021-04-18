""" Payment app. """

# Django
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PaymentConfig(AppConfig):
    """ Payment app config. """
    name = 'payment'

    def ready(self):
        from .signals import assign_payment_type_prices
        post_migrate.connect(assign_payment_type_prices, sender=self)
