from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, HTML
from django import forms
from django.urls import reverse

from .models import Notes


class DateInput(forms.DateInput):
	input_type = 'date'
	format_key = '%Y-%m-%d'


class CreateNoteForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.add_input(Submit('submit', 'Create'))

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
		super().__init__(*args, **kwargs)
		self.url = reverse("delete_note", args=[self.instance.id])
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Update')),
		self.helper.add_input(Button(
			'delete',
			'Delete',
			onclick='window.location.href="{}"'.format(self.url)))

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
