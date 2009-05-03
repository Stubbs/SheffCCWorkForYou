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
from google.appengine.ext import db
from councilwatch.core.models import Councillor

class CouncillorInfoParser():
	"""Receives a copy of the Ward Info page and parses out the councillors for that ward."""
	
	def __init__(self, xmlString, ward):
		councillors = []
		
		self.dom = html.fromstring(xmlString)
		
		try:
			divs = self.dom.xpath("//div[@class='NormalBodyBold']")
		except IndexError, message:
			print "Index out of range (%s)" % message
			
		
		for elem in divs:
			if elem.text.startswith('Cllr'):
				try:
					# Dig out all thus councilors info.
					name = elem.text.split(':')[1]
					party = list(elem.getnext())[0].text
					telephones = list(elem.getnext().getnext().getnext())[0].tail.lstrip()
					email = list(elem.getnext().getnext().getnext().getnext())[1].text
					surgery = elem.getnext().getnext().getnext().getnext().getnext().getnext().getnext().text_content()
					address = elem.getnext().getnext().getnext().getnext().getnext().getnext().getnext().getnext().getnext().getnext().text

					# Update if the concillor exists.
					query = Councillor.all()
					query.filter('name =', name)
					result = query.fetch(1)

					# TODO: Update the councillor
					if len(result) == 0:
						councillor = Councillor(name=name, ward = ward, party = party, telephone_home = telephones, email = email, surgery = surgery, address = address)
						councillors.append(councillor)
				except Exception, message:
					print message
					continue

		if len(councillors) > 0:
			db.put(councillors)
	
class CouncillorInfo(httplib.HTTPConnection):
	"""This class downloads the ward info page and parses out the councillors and their info"""
	host = 'www.sheffield.gov.uk'
	
	def __init__(self, url, ward):
		httplib.HTTPConnection.__init__(self, self.host)
		self.request("GET", url)
		
		self.wardparser = CouncillorInfoParser(self.getresponse().read(), ward)
