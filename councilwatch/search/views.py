from django.shortcuts import render_to_response
from councilwatch.core.models import *

def index(request):
	if request.POST:
		try:
			ward = WardPostcode.all().filter('postcode =', request.POST['postcode'].replace(' ', '').upper())[0].ward
			councillors = Councillor.all().filter('ward =', ward)
			not_found = False
		except IndexError:
			not_found = True
			return render_to_response('search/index.html', {'not_found': not_found})
			
		return render_to_response('search/index.html', {'results': True, 'councillors': councillors, 'ward': ward, 'not_found': not_found})
	else:
		return render_to_response('search/index.html', {})
