from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
 
class Cart(models.Model):
    """
    Simple cart object
    """
    user = models.ForeignKey(User, null=True)
    date_added = models.DateTimeField(default=datetime.now)
 
class CartItem(models.Model):
    """
    Association between a cart and a product
    """
    cart = models.ForeignKey(Cart)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    quantity = models.IntegerField()

