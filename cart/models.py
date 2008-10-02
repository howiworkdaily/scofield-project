from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


from scofield.product.models import Product


class Cart(models.Model):
    """
    A cart to store cart items
    """
    date_created = models.DateTimeField(default=datetime.now)
    customer = models.ForeignKey(User, blank=True, null=True, verbose_name='Customer')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now)

