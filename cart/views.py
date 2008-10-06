from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from utils import bad_or_missing
from django.contrib.auth.models import User

from product.models import *


def add_to_cart(request, product_slug, template_name="product/details.html"):
    """
    Product Detail View
    """

    try:
        product = Product.objects.get(published=True, slug=product_slug)
    except Product.DoesNotExist:
        return bad_or_missing(request, 'The product or page you have requested is not in the catalog.')

    related = product.related_products.all()

    return render_to_response(template_name, {
        "product": product, 
        "related": related,
    }, context_instance=RequestContext(request))
upload = login_required(upload)
