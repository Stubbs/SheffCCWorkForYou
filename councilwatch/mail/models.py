from google.appengine.ext import db
from google.appengine.api import mail

from datetime import date

# Create your models here.

class Email(db.Model):
	from_name = db.StringProperty(required=True)
	from_address = db.EmailProperty(required=True)
	to_address = db.ListProperty(db.Email)
	body = db.TextProperty(required=True)
	sent = db.BooleanProperty()
	sent_date = db.DateProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	replied = db.BooleanProperty()
	replied_date = db.DateProperty()
	
	def send(self):
		mail.send_mail(sender="Sheffield County Council Work For You <sheffccworkforyou@googlemail.com>", to=self.to_address, reply_to="%s <%s>" % (self.from_name, self.from_address), body=self.body, subject="A question from your residents, %s" % self.from_name)
		
		self.sent = True
		self.sent_date = date.today()
		
		self.put()