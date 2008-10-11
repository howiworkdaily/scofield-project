from django.conf.urls.defaults import *


urlpatterns = patterns('cart.views',
    url(r'^add/$', 'add', {}, 'add_to_cart'),
    url(r'^show/$', 'show', {}, 'show_cart'),
 )
