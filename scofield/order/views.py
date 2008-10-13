from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from account.models import *
from cart.models import *
from order.forms import AddressForm 
from account.forms import LoginForm

def checkout(request, template_name="order/checkout.html"):
    """
    Displays the customer info form for checkout
    """
    loginform = LoginForm()
    addressform = AddressForm()

    if request.method == 'POST':
        addressform = AddressForm(request.user, request.POST)
        if addressform.is_valid():
            addressform.save()

    return render_to_response(template_name, {
        "loginform": loginform,
        "addressform": addressform,
    }, context_instance=RequestContext(request)) 
