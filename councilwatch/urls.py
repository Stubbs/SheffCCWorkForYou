from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^councilwatch/', include('councilwatch.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
	(r'^search/', include('councilwatch.search.urls')),
	(r'^mail/', include('councilwatch.mail.urls')),
)
