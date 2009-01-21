from django.conf.urls.defaults import *
from django.conf import settings

import booking.calendars
yeartable = booking.calendars.Year(2009)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_booking/', include('django_booking.foo.urls')),
    (r'^calendar/', 'django.views.generic.simple.direct_to_template',
     {'template': 'calendar.html',
      'extra_context':{'yeartable':yeartable}}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    # themes
    (r'^themes/', include('django_booking.themes.urls')),
    # static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
