from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from product.models import Product

def get_product(request, product_slug, template_name="product/details.html"):
    """
    Product Detail View
    """

    try:
        product = Product.objects.get(published=True, slug=product_slug)
    except Product.DoesNotExist:
        return bad_or_missing(request, 'The product or page you have requested is not in the catalog.')
    print product

    return render_to_response(template_name, {
        "product": product, 
    }, context_instance=RequestContext(request))
