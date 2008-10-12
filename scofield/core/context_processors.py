from django.contrib.auth.models import User 
from category.models import *
from manufacturer.models import *

def dynamic_menus(request): 
    # TODO: move these into templatetags to reduce the number of queries
    return {
        'manufacturers': Manufacturer.objects.filter(published=True),
    }
