from django import http
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from utils import bad_or_missing

from category.models import *

def get_category(request, category_slug, template_name="category/list.html"):
    """
    Category Product List View
    """

    try:
        category = Category.objects.get(published=True, slug=category_slug)
    except Category.DoesNotExist:
        return bad_or_missing(request, 'The category you have requested is not in the catalog.')
    
    return render_to_response(template_name, {
        "category": category, 
    }, context_instance=RequestContext(request))

