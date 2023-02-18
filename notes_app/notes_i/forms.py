from django import forms
from .models import Notes


class DateInput(forms.DateInput):
	input_type = 'date'
	format_key = '%Y-%m-%d'


class CreateNoteForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateNoteForm, self).__init__(*args, **kwargs)
		self.fields['reminder'].required = False
		self.fields['category'].required = False

	class Meta:
		model = Notes
		fields = [
			'tittle',
			'text',
			'reminder',
			'category',
			]

		widgets = {
			'reminder': DateInput
		}


class UpdateNoteForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UpdateNoteForm, self).__init__(*args, **kwargs)
		self.fields['reminder'].required = False
		self.fields['category'].required = False

	class Meta:
		model = Notes
		fields = [
				  'tittle',
				  'text',
				  'reminder',
				  'category'
				  ]

		widgets = {
			'reminder': DateInput
		}
