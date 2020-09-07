from django.urls import path
from .views import (
    PaymentListView, 
    PaymentDetailView, 
    PaymentCreateView, 
    PaymentUpdateView,
    PaymentDeleteView,
)
from . import views

urlpatterns = [
    path('', PaymentListView.as_view(), name='index'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('<int:pk>/update', PaymentUpdateView.as_view(), name='payment-update'),
    path('<int:pk>/delete', PaymentDeleteView.as_view(), name='payment-delete'),
    path('new/', PaymentCreateView.as_view(), name='payment-create'),
]