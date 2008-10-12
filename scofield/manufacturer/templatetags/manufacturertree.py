from django import template
from django.contrib.contenttypes.models import ContentType
from manufacturer.models import Manufacturer
register = template.Library()

def manufacturertree(context):
    manufacturers = Manufacturer.objects.filter(published=True)
    return {
        'manufacturers': manufacturers, 
    }


register.inclusion_tag('manufacturertree.html', takes_context=True)(manufacturertree)

