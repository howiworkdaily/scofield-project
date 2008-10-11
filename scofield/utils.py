from django import http
from django.template import RequestContext
from django.template import loader

def bad_or_missing(request, msg):
    """
    Return an HTTP 404 response for a product request that does not exist.
    The 'msg' parameter gives the message for the main panel on the page.
    """
    template = loader.get_template('404.html')
    context = RequestContext(request, {'message': msg})
    return http.HttpResponseNotFound(template.render(context))
