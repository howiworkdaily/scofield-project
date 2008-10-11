from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from manufacturer.models import *

def get_manufacturer(request, manufacturer_slug, template_name="manufacturer/list.html"):
    """
    Products list for manufacturer
    """

    try:
        manufacturer = Manufacturer.objects.get(published=True, slug=manufacturer_slug)
    except manufacturer.DoesNotExist:
        return bad_or_missing(request, 'The manufacturer you have requested is not in the catalog.')

    return render_to_response(template_name, {
        "manufacturer": manufacturer, 
    }, context_instance=RequestContext(request))
