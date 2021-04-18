""" Payment forms. """

# Django
from django import forms

# Models
from .models import PaymentType

class PaymentTypeForm(forms.ModelForm):
    """ Payment Type form to adjust price for each payment type. """
    
    class Meta:
        """ Meta class. """
        model = PaymentType
        fields = '__all__'
        widgets = {'payment_code': forms.HiddenInput()}