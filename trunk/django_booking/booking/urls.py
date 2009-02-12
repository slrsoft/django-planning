from django.conf.urls.defaults import *

from django.conf import settings
import os.path

import views

urlpatterns = patterns('',
    (r'^.*login/$', 'django.contrib.auth.views.login', {'template_name':'admin/login.html'}),
    (r'^$', views.display, {'year':None, 'template':'calendar_ro.html'}),
    (r'^(?P<year>\d{4})/$', views.display, {'template':'calendar_ro.html'}),
    (r'^(?P<year>\d{4})/edit/$', views.edit, {'template':'calendar.html'}),
    (r'^(?P<year>\d{4})/filter/(?P<id>\d+)/(?P<value>true|false)/$', views.display_filter),
    (r'^(?P<year>\d{4})/edit/set/(?P<id>\d+)/(?P<days>.*)/$', views.edit_set),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
    )
