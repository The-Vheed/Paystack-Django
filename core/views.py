from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.conf import settings

# Create your views here.

def initiate_payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            context = {
                'payment': payment,
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
            }
            return render(request, 'make_payment.html', context)
    else:
        payment_form = PaymentForm()
        context = {
            'payment_form': payment_form
        }
        return render(request, 'initiate_payment.html', context)

def verify_payment(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Payment Verified')
    else:
        messages.error(request, 'Payment Verification Failed')
    return redirect('initiate-payment')