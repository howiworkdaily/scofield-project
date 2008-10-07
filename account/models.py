from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Account(models.Model):
    
    user = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    
    
    def __unicode__(self):
        return self.user.username



def create_account(sender, instance=None, **kwargs):
    if instance is None:
        return
    account, created = Account.objects.get_or_create(user=instance)

post_save.connect(create_account, sender=User)
