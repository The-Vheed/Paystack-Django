from dataclasses import fields
from django import forms
from .models import *


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'email']