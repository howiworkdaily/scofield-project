from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from product.models import Product


class Wishlist(models.Model):
    """
    model to store a customer's wishlist items
    """
    customer = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    date_added = models.DateTimeField(default=datetime.now)

