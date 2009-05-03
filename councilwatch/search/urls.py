from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'councilwatch.search.views.index'),
)
