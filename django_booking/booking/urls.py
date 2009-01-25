from django.conf.urls.defaults import *

from django.conf import settings
import os.path

import views

import calendars
yeartable = calendars.Year(2009)

urlpatterns = patterns('',
    (r'^(?P<year>\d{4})/$', views.display, {'template':'calendar_ro.html'}),
    (r'^calendar/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'calendar.html',
      'extra_context':{'yeartable':yeartable}}),
    (r'^calendar/add/$', views.add_booking),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
    )
