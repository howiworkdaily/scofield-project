from django.contrib.auth.models import User 
from category.models import *
from manufacturer.models import *

def dynamic_menus(request): 
    return {
        'manufacturers': Manufacturer.objects.filter(published=True),
        'categories': Category.objects.filter(published=True),
    }
