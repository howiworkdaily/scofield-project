from django.conf.urls.defaults import *


urlpatterns = patterns('order.views',
    url(r'^checkout/$', 'checkout', {}, 'scofield_checkout_step_one'),
 )
