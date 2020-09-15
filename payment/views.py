from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Payment.objects.all()
        else:
            return Payment.objects.filter(athlete=self.request.user)

class PaymentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Payment
    fields = ['payment_type', 'amount', 'reference', 'athlete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear pago'
        return context

    def test_func(self):
        return self.request.user.is_staff

class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['payment_type', 'amount', 'reference', 'athlete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar pago'
        return context

    def test_func(self):
        return self.request.user.is_staff

class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Payment
    success_url = '/payment/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Elminar pago'
        return context

    def test_func(self):
        return self.request.user.is_staff
