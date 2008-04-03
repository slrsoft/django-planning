from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^planning/', include('planning.foo.urls')),

    # Uncomment this for admin:
     (r'^admin/', include('django.contrib.admin.urls')),
     (r'^$', 'planning.cal.views.main'),
)
