from django.conf.urls.defaults import *


urlpatterns = patterns('samosit.projects.views',
                       (r'^$', 'index'),
)
