from django import newforms as forms

class EmailForm(forms.Form):
	from_field = forms.EmailField(required=True, label='Enter your email address')
	from_name = forms.CharField(required=True, label='Enter your name')
	body = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': '15', 'cols': '70'}), label='Type your message here')