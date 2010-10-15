from django.conf.urls.defaults import *


urlpatterns = patterns('samosit.pages.views',
                       (r'^(?P<page_id>\d+)/([a-zA-Z0-9_.-]{0,40})$', 'detail'),
)
