from django import template
from django.contrib.contenttypes.models import ContentType
from category.models import Category
register = template.Library()

def categorytree(context):
    categories = Category.objects.filter(published=True)
    return {
        'categories': categories, 
    }


register.inclusion_tag('categorytree.html', takes_context=True)(categorytree)
