from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from product.models import *

def home(request, template_name="home_page.html"):
    """
    Home page featured products
    """

    product = Product.objects.filter(published=True, is_featured=True)

    return render_to_response(template_name, {
        "product": product,
    }, context_instance=RequestContext(request))

def get_product(request, product_slug, template_name="product/details.html"):
    """
    Product Detail View
    """
    try:
        product = Product.objects.get(published=True, slug=product_slug)
    except Product.DoesNotExist:
        return bad_or_missing(request, 'The product or page you have requested is not in the catalog.')

    related = product.related_products.all()
    images = ProductImage.objects.filter(product=product.id)

    return render_to_response(template_name, {
        "product": product, 
        "related": related,
        "images": images,
    }, context_instance=RequestContext(request))
