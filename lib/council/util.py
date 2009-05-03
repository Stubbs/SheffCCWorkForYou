#!/usr/bin/env python
# encoding: utf-8
"""
util.py

Created by Stuart Grimshaw on 2009-03-21.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
from councilwatch.core.models import Ward, Councillor, WardPostcode
from google.appengine.ext import db

def truncate_ward():
	"""Unfortunatly, you can't just truncate the tables on app engine, so this method deletes them 300
	at a time, scaling that back if it gets an error."""
	
	print "Deleting WardPostcode objects"
	fetchRows = 300
	rows = WardPostcode.all().fetch(fetchRows)
	while len(rows) > 0:
		try:
			db.delete(rows)
			print "Deleted %s WardPostcode objects" % len(rows)
		except db.Timeout:
			fetchRows = fetchRows - 50
			print "Timeout, reducing rows fetched to %s" % fetchRows
			if fetchRows <= 0:
				print "Unable to fetch rows"
				exit(0)

		rows = WardPostcode.all().fetch(fetchRows)
	
	print "Deleting Ward objects"
	fetchRows = 300
	rows = Ward.all().fetch(fetchRows)
	while len(rows) > 0:
		try:
			db.delete(rows)
			print "Deleted %s Ward objects" % len(rows)
		except db.Timeout:
			fetchRows = fetchRows - 50
			print "Timeout, reducing rows fetched to %s" % fetchRows

			if fetchRows <= 0:
				print "Unable to fetch rows"
				exit(0)
		
		rows = Ward.all().fetch(fetchRows)

def truncate_councillor():
	"""Unfortunatly, you can't just truncate the tables on app engine, so this method deletes them 300
	at a time, scaling that back if it gets an error."""
	
	print "Deleting Councillor objects"
	fetchRows = 300
	rows = Councillor.all().fetch(fetchRows)
	while len(rows) > 0:
		try:
			db.delete(rows)
			print "Deleted %s Councillor" % len(rows)
		except db.Timeout:
			fetchRows = fetchRows - 50
			print "Timeout, reducing rows fetched to %s" % fetchRows

			if fetchRows <= 0:
				print "Unable to fetch rows"
				exit(0)
		
		rows = Councillor.all().fetch(fetchRows)	

def truncate_all():
	truncate_ward()
	truncate_councillor()
