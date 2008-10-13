from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from contact.models import *
from cart.models import *

class checkout(request,template_name="order/checkout.html"):
    """
    Displays the customer info form for checkout
    """
    return render_to_response(template_name, {
        "category": category, 
    }, context_instance=RequestContext(request)) 
