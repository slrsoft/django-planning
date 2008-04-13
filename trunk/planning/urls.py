from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^planning/', include('planning.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^$', 'planning.cal.views.main'),
    (r'^add/$', 'planning.cal.views.add_planning', {'redirect':'../planning/%d/edit/'}),
    (r'^planning/(?P<id>.*)/edit/$', 'planning.cal.views.edit', {'template':'edit.html'}),
    (r'^planning/(?P<code>[^/]+)/$', 'planning.cal.views.main'),
)
