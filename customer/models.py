from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Customer(models.Model):
    """
    Model to store the customer
    """

    user = models.ForeignKey(User)
    firstname = models.CharField('First Name', max_length=100, null=False, blank=False)
    lastname = models.CharField('Last Name', max_length=100, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    date_added = models.DateTimeField(default=datetime.now)


PHONE_CHOICES = (
    ('Work', 'Work'),
    ('Home', 'Home'),
    ('Mobile', 'Mobile'),
)

class Phonenumber(models.Model):
    """
    Customer phone numbers
    """

    customer = models.ForeignKey(Customer)
    type = models.CharField('Type of Number', choices=PHONE_CHOICES, blank=False, null=False, max_length=100)
    phone = models.CharField('Phone Number', blank=True, max_length=30)
    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Numbers'

class Address(models.Model):
    """
    Addresses for customer.  Both shipping and billing
    """

    customer = models.ForeignKey(Customer)
    street1 = models.CharField('Street', max_length=100)
    street2 = models.CharField('Street', max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    zip_code = models.CharField('Zip Code', max_length=25)
    default_shipping = models.BooleanField('Default Shipping Address', default=False)
    default_billing = models.BooleanField('Default Billing Address', default=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
