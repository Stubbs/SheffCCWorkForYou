#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stuart Grimshaw on 2009-03-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys,os
import httplib
from lxml import html, etree

class Councillor():
	name = ''
	party = ''
	ward = ''
	telephone = ''
	email = ''
	surgeryinfo = ''
	address = ''

class CouncillorInfoParser():
	"""Receives a copy of the Ward Info page and parses out the councillors for that ward."""
	
	councillors = []
	
	def __init__(self, xmlString):
		self.dom = html.fromstring(xmlString)
		
		divs = self.dom.xpath("//div[@class='NormalBodyBold']")
		
		for elem in divs:
			if elem.text.startswith('Cllr'):
				self.councillors.append(elem.text)
				print elem.text
	
	
class CouncillorInfo(httplib.HTTPConnection):
	"""This class downloads the ward info page and parses out the councillors and their info"""
	host = 'www.sheffield.gov.uk'
	
	def __init__(self, url):
		httplib.HTTPConnection.__init__(self, self.host)
		self.request("GET", url)
		
		self.wardparser = CouncillorInfoParser(self.getresponse().read())
