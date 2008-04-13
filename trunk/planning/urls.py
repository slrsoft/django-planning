from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    # Example:
    # (r'^planning/', include('planning.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^$', 'planning.cal.views.main'),
    (r'^add/$', 'planning.cal.views.add_planning', {'redirect':'../planning/%d/edit/'}),
    (r'^planning/(?P<id>.*)/edit/$', 'planning.cal.views.edit', {'template':'edit.html'}),
    (r'^planning/(?P<id>.*)/addtype/$', 'planning.cal.views.add_type', {'template':'type.html'}),
    (r'^planning/(?P<code>[^/]+)/$', 'planning.cal.views.planning'),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
