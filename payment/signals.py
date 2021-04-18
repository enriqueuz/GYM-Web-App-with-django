""" Payment signals. """

# Models
from .models import PaymentType

def assign_payment_type_prices(sender, interactive=True, **kwargs):
    """ After running 'migrate' 
    Prompt the user to input the price of each payment type. """

    for choice in PaymentType.PAYMENT_CHOICES:
        amount = float(input(f'Enter {choice[1]} price: '))
        PaymentType.objects.create(
            payment_code=choice[0],
            amount=amount
            )