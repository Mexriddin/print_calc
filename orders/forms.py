from django.forms import ModelForm
from .models import Order

""" Order Form """
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['total_price', 'price_for_one']




