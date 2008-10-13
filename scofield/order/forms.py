from django import forms
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

from order.models import Order

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Order
        exclude = ('customer', 'date_added')
        
    def __init__(self, user=None, *args, **kwargs):
        self.customer = user
        super(AddressForm, self).__init__(*args, **kwargs)
