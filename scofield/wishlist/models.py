from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from scofield.product.models import Product

class Wishlist(models.Model):
    """
    Customer's Wishlist Base Class
    """
    customer = models.ForeignKey(User)
    date_added = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=20, default='General')

    class Meta:
        ordering = ['date_added', 'customer']
        unique_together = ('customer','name')


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


