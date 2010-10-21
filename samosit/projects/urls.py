from django.conf.urls.defaults import *


urlpatterns = patterns('samosit.projects.views',
                       url(r'^$', 'index', name="project_index"),
                       url(r'^(?P<project_id>\d+)/(?P<slug>[a-zA-Z0-9_.-]{0,40})$', 'detail', name="project_detail")
)
