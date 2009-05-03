from google.appengine.api import mail
from google.appengine.ext import db
from django.shortcuts import render_to_response
from councilwatch.core.models import *
from councilwatch.mail.models import Email
from councilwatch.mail.forms import EmailForm

def index(request):
	if request.POST:
		# Create the temporary record.
		form = EmailForm(request.POST)
		
		success = False
		
		if(form.is_valid()):
			to_list = [db.Email(form.clean_data['from_field'].lower())]
			email = Email(from_name=form.clean_data['from_name'], from_address=form.clean_data['from_field'].lower(), body=form.clean_data['body'], to_address=to_list)
			email.put()
			
			body = """
Dear %s,

Before we send your message to your councillors you must confirm your email address by clicking on the link below.

http://sheffccwatch.appspot.com/mail/confirm/%s/

If you do not click on the link then the email will be deleted after a week, and the link will stop working.
""" % (form.clean_data['from_name'], email.key())
			
			message = mail.send_mail(sender="Sheffield County Council Work For You <sheffccworkforyou@googlemail.com>", to=form.clean_data['from_field'].lower(), body = body, subject="Confirm your email address")

			form = EmailForm()
			
			success = True

		return render_to_response('mail/index.html', {'email_form': form, 'success': True})
	else:
		email_form = EmailForm()
		return render_to_response('mail/index.html', {'email_form': email_form })
		
def confirm(request, email_key):
	# retrieve the email and send it, then mark the mail as sent.
	email = Email.get(email_key)
	email.send()
	
	return render_to_response('mail/thanks.html', {'councillors': email.to_address })