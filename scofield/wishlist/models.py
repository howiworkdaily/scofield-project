from django.db import models
from django.contrib.auth.models import User


class Wishlist(models.Model):
    """
    model to store a customer's wishlist items
    """
