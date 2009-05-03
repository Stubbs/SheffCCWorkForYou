from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'councilwatch.mail.views.index'),
	(r'^confirm/(?P<email_key>.*?)/$', 'councilwatch.mail.views.confirm'),
)
