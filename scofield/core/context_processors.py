from django.contrib.auth.models import User 
from category.models import *
from manufacturer.models import *

def dynamic_menus(request): 
    """
    If middleware is your thing and you don't mind the overhead of unneeded queries in views that don't
    require these menus, uncomment the following and add to your MIDDLEWARE_CLASSES, otherwise use the
    templatetags.
    """

    return {
        # 'manufacturers': Manufacturer.objects.filter(published=True),
        # 'categories': Category.objects.filter(published=True),
    }
