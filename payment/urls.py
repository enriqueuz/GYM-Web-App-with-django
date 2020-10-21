from django.urls import path
from .views import (
    PaymentListView, 
    PaymentDetailView, 
    PaymentCreateView, 
    PaymentUpdateView,
    PaymentDeleteView,
    payment_type_update,
    PaymentTypeListView,
    get_amount,
    get_type_amount,
)
from . import views

urlpatterns = [
    path('', PaymentListView.as_view(), name='index'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('<int:pk>/update', PaymentUpdateView.as_view(), name='payment-update'),
    path('<int:pk>/delete', PaymentDeleteView.as_view(), name='payment-delete'),
    path('new/', PaymentCreateView.as_view(), name='payment-create'),
    path('type/', PaymentTypeListView.as_view(), name= 'payment_type-list'),
    path('type/update/', payment_type_update, name='payment_type-update'),
    path('get/ajax/get_amount', get_amount, name= "get-amount"),
    path('get/ajax/get_type_amount', get_type_amount, name= "get-type-amount"),
]