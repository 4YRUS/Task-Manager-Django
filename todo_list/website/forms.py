from django import forms 
from .models import record

class add_record_form(forms.ModelForm):

	task= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': "Enter the task here", "class": "form-control"}),label='')
	status= forms.CharField(initial='TODO',required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control" ,}),label='')
	class Meta:
		model=record
		exclude=('user',)
