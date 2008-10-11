from django.conf.urls.defaults import *


urlpatterns = patterns('category.views',
    url(r'^(?P<category_slug>[-\w]+)/$', 'get_category', {}, 'scofield_category'),
 )
