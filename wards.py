#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stuart Grimshaw on 2009-03-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
from lxml import html, etree
from councillors import CouncillorInfo

# Load the App Engine db class.
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")
from google.appengine.ext import db

class ParseWards:
	def __init__(self, url):
		self.wards = []
		self.dom = html.fromstring(url)
		print "Parsed index page."
		self.parseWards()

	def parseWards(self):
		# Find the map element with the ID "map"
		mapNode = self.dom.get_element_by_id('map')

		for action,elem in etree.iterwalk(mapNode, tag='area'):
			print "Downloading %s" % elem.get('alt')
			self.wards.append(elem.get('alt'))
			CouncillorInfo(elem.get('href'))

class ParseWardsTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()