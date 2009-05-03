from google.appengine.ext import db

# Create your models here.

class Ward(db.Model):
	name = db.StringProperty(required = True)
	
class WardPostcode(db.Model):
	ward = db.ReferenceProperty(Ward, required = True)
	postcode = db.StringProperty(required = True)
	
class Councillor(db.Model):
	name = db.StringProperty(required = True)
	party = db.StringProperty(required = True)
	telephone_home = db.StringProperty()
	telephone_townhall = db.StringProperty()
	ward = db.ReferenceProperty(Ward, required = True)
	email = db.EmailProperty(required = True)
	surgery = db.TextProperty()
	address = db.PostalAddressProperty()