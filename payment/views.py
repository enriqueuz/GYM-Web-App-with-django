from django.shortcuts import render
from .models import Payment
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'payments': Payment.objects.all()
    }
    return render(request, 'payment/index.html', context)