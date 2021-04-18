""" Payment views """

# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)

# Forms
from .forms import PaymentTypeForm

# Models
from .models import Payment, PaymentType

# Utils
from utils.mixins import PageTitleMixin

class PaymentDetailView(DetailView):
    """ Payment detail view. """

    model = Payment


class PaymentListView(LoginRequiredMixin, ListView):
    """ Payment list view. """

    model = Payment
    context_object_name = 'payments'
    ordering = ['-date']

    def get_queryset(self):
        """ If user is not staff only show his payments. """
        if self.request.user.is_staff == True:
            return Payment.objects.all()
        else:
            return Payment.objects.filter(athlete=self.request.user)


class PaymentCreateView(PageTitleMixin, 
                        LoginRequiredMixin, 
                        UserPassesTestMixin, 
                        CreateView):
    """ Payment create view. """

    model = Payment
    fields = ['payment_type', 'reference', 'athlete']
    page_title = 'Crear pago'

    def test_func(self):
        return self.request.user.is_staff


class PaymentUpdateView(PageTitleMixin, 
                        LoginRequiredMixin, 
                        UserPassesTestMixin, 
                        UpdateView):
    """ Payment update view. """

    model = Payment
    fields = ['payment_type', 'reference', 'athlete']
    page_title = 'Actualizar pago'

    def test_func(self):
        return self.request.user.is_staff


class PaymentDeleteView(PageTitleMixin, 
                        LoginRequiredMixin, 
                        UserPassesTestMixin, 
                        DeleteView):
    """ Payment delete view. """
    
    model = Payment
    success_url = '/payment/'
    page_title = 'Elminar pago'

    def test_func(self):
        return self.request.user.is_staff


class PaymentTypeListView(PageTitleMixin, LoginRequiredMixin, ListView):
    """ Payment type list view. """

    model = PaymentType
    page_title = 'lista de tipos de pago'


class PaymentTypeDetailView(LoginRequiredMixin, 
                            UserPassesTestMixin, 
                            DetailView):
    """ Payment type detail view. """

    model = PaymentType
    page_title = 'Tipo de pago'


def payment_type_update(request):
    """ Payment type update view. """

    template ='payment/paymenttype_form.html'
    payment_types = PaymentType.objects.all()

    if request.method == 'POST':
        post = request.POST.copy()
        payment_type_code = post['payment_code']
        type_instance = get_object_or_404(PaymentType, payment_code=payment_type_code)
        
        t_form = PaymentTypeForm(request.POST, instance=(type_instance))

        if t_form.is_valid():
            t_form.save()
            messages.success(request, f'El tipo de pago ha sido actualizado')
            return redirect('index')
    else:
        t_form = PaymentTypeForm()

    context = {
        'payment_types': payment_types,
        'form': t_form
    }

    return render(request, template, context)


def get_amount(request):
    """ Get the price for the payment """
    
    if request.is_ajax and request.method == "GET":
        current_payment = request.GET.get("payment_type")
        current_amount = get_object_or_404(PaymentType, pk=current_payment).amount
        return JsonResponse({"current_amount":current_amount}, status=200)
    
    return JsonResponse({}, status = 400)


def get_type_amount(request):
    """ Get the price for the payment type """

    if request.is_ajax and request.method == "GET":
        current_payment_type = request.GET.get("code")
        current_amount = get_object_or_404(PaymentType, payment_code=current_payment_type).amount
        return JsonResponse({"current_amount":current_amount}, status=200)
    
    return JsonResponse({}, status = 400)