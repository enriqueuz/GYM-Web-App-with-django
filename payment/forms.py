from django import forms
from .models import PaymentType

class PaymentTypeForm(forms.ModelForm):
    
    class Meta:
        model = PaymentType
        fields = '__all__'
        widgets = {'payment_code': forms.HiddenInput()}