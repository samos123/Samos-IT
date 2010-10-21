from django.conf.urls.defaults import *


urlpatterns = patterns('samosit.pages.views',
                       url(r'^(?P<page_id>\d+)/(?P<slug>[a-zA-Z0-9_.-]{0,40})$', 'detail', name='page_detail'),
)
