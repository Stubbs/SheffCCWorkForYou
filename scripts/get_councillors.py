#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stuart Grimshaw on 2009-03-14.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.

Script to download a list of all councillors.
"""

import sys

sys.path.append("../")
sys.path.append("../lib")

import os
import httplib
from council.wards import ParseWards
from google.appengine.ext.remote_api import remote_api_stub

APP_NAME = 'sheffccwatch'
os.environ['AUTH_DOMAIN'] = 'gmail.com'  
os.environ['USER_EMAIL'] = 'stuart.grimshaw@gmail.com'

def auth_func():  
	return ('your_username@googlemail.com', 'your_password')

remote_api_stub.ConfigureRemoteDatastore(APP_NAME,  '/remote_api/', auth_func, servername='localhost:8084')

def main():
	print "Getting ward list"
	host = "www.sheffield.gov.uk"
	councillorURL = "/your-city-council/councillors"
	
	conn = httplib.HTTPConnection(host)
	conn.request("GET", councillorURL)
	r = conn.getresponse()

	print "Retrieved ward index page"

	councillorparser = ParseWards(r.read())

if __name__ == '__main__':
	main()

