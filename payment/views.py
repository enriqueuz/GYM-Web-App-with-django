from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Payment, PaymentType
from django.http import JsonResponse
from .forms import PaymentTypeForm
from django.contrib import messages

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
    fields = ['payment_type', 'reference', 'athlete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear pago'
        return context

    def test_func(self):
        return self.request.user.is_staff

class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['payment_type', 'reference', 'athlete']

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

def get_amount(request):
    #Get the price for the payment
    if request.is_ajax and request.method == "GET":
        current_payment = request.GET.get("payment_type")
        current_amount = PaymentType.objects.get(pk=current_payment).amount
        return JsonResponse({"current_amount":current_amount}, status=200)
    
    return JsonResponse({}, status = 400)

class PaymentTypeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = PaymentType
    
    def test_func(self):
        return self.request.user.is_staff

class PaymentTypeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PaymentType

def payment_type_update(request):
    template ='payment/paymenttype_form.html'
    payment_types = PaymentType.objects.all()

    if request.method == 'POST':
        post = request.POST.copy()
        payment_type_code = post['payment_code']
        type_instance = PaymentType.objects.get(payment_code=payment_type_code)
        
        t_form = PaymentTypeForm(request.POST, instance=(type_instance))

        if t_form.is_valid():
            t_form.save()
            messages.success(request, f'El tipo de pago ha sido actualizado')
            return redirect('index')
    else:
        t_form = PaymentTypeForm()

    context = {
        'payment_types': payment_types,
        'form':t_form
    }

    return render(request, template, context)         

def get_type_amount(request):
    #Get the price for the payment type
    if request.is_ajax and request.method == "GET":
        current_payment_type = request.GET.get("code")
        current_amount = PaymentType.objects.get(payment_code=current_payment_type).amount
        return JsonResponse({"current_amount":current_amount}, status=200)
    
    return JsonResponse({}, status = 400)