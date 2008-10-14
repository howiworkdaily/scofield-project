from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from scofield.product.models import Product


class Wishlist(models.Model):
    """
    Customer's Wishlist
    """
    customer = models.ForeignKey(User)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['date_added', 'customer']

class WishlistItem(models.Model):
    """
    An instance of a product added to the wishlist
    """
    
    wishlist = models.ForeignKey(Wishlist)
    product = models.ForeignKey(Product)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'


