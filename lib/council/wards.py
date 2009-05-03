#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stuart Grimshaw on 2009-03-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.

"""

import sys

sys.path.append('../lib')
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")

import os
import unittest
from lxml import html, etree
from councillors import CouncillorInfo
from councilwatch.core.models import Ward

class ParseWards:
	def __init__(self, url):
		self.wards = dict()
		self.dom = html.fromstring(url)
		print "Parsed index page."
		self.parseWards()

	def parseWards(self):
		# Find the map element with the ID "map"
		mapNode = self.dom.get_element_by_id('map')

		for action,elem in etree.iterwalk(mapNode, tag='area'):
			print "Downloading %s" % elem.get('alt')
			
			# Find the ward object for this ward.
			if(self.wards.get(elem.get('alt'))):
				ward = self.wards.get(elem.get('alt'))
			else:
				try:
					ward = Ward.all().filter('name =', elem.get('alt')).fetch(1)[0]
					self.wards[elem.get('alt')] = ward
				except NameError, message:
					print "Unable to find %s ward (%s)" % (elem.get('alt'), message)
					continue
			
			CouncillorInfo(elem.get('href'), ward)

class ParseWardsTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()