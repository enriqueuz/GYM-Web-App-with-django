from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment

def index(request):
    context = {
        'payments': Payment.objects.all()
    }
    return render(request, 'payment/index.html', context)

class PaymentDetailView(DetailView):
    model = Payment

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payment/index.html' # app/model_viewtype.html
    context_object_name = 'payments'
    ordering = ['-date']

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['payment_type', 'amount', 'reference', 'athlete']

class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    fields = ['payment_type', 'amount', 'reference', 'athlete']

class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    success_url = '/payment/'