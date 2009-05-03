#!/usr/bin/env python
# encoding: utf-8
"""
import_ward_postcodes.py

Created by Stuart Grimshaw on 2009-03-19.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import csv

sys.path.append("../")
sys.path.append("../lib")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")

from councilwatch.core.models import Ward, WardPostcode
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db
import council.util

APP_NAME = 'sheffccwatch'
os.environ['AUTH_DOMAIN'] = 'gmail.com'  
os.environ['USER_EMAIL'] = 'stuart.grimshaw@gmail.com'

def auth_func():  
	return ('your_username@googlemail.com', 'your_password')
	
remote_api_stub.ConfigureRemoteDatastore(APP_NAME,  '/remote_api/', auth_func, servername='localhost:8084')

def main():
	wards = dict()
	wardpostcodes = []
	streets = csv.DictReader(open('data/streets.txt'))

	council.util.truncate_all()

	for row in streets:
		if row.get('All Post Codes'):
			postcodes = row.get('All Post Codes').split(',')
			wardName = row.get('Ward')
			for postcode in postcodes:
				if wards.get(wardName) is None:
					ward = Ward(name = wardName.replace('&', 'and'))
					ward.put()
					wards[wardName] = ward
				else:
					ward = wards.get(wardName)

				wardpostcodes.append(WardPostcode(ward = ward, postcode = postcode.strip().replace(' ', '').upper()))
				
				if len(wardpostcodes) > 99:
					print "Saving %s streets" % len(wardpostcodes)
					db.put(wardpostcodes)
					wardpostcodes = []
	
	if len(wardpostcodes) > 0:
		print "Saving %s streets" % len(wardpostcodes)
		db.put(wardpostcodes)
	
	print "Created %s wards" % len(wards)

if __name__ == '__main__':
	main()

