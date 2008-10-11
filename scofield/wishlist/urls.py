from django.conf.urls.defaults import *


urlpatterns = patterns('wishlist.views',
    url(r'^add/$', 'add', {}, 'add_to_wishlist'),
    url(r'^show/$', 'show', {}, 'show_wishlist'),
 )
