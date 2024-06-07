from django import forms
from .models import Order
class OrderForms(forms.ModelForm):
    class Meta:
        model=Order
        fields=['uname','date','email','number','food','Restaurant','drinks','soups','dish','order']