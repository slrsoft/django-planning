from django.conf.urls.defaults import *
from django.conf import settings

import os.path

urlpatterns = patterns('',
    (r'^preview/yast', 'django.views.generic.simple.direct_to_template',
     {'template': 'themes/yast/base.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
    )
