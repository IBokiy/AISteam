from .models import Notes, Category
from django import forms
import django_filters


class NotesFilter(django_filters.FilterSet):
	category = django_filters.ModelChoiceFilter(
		queryset=Category.objects.all(),
		field_name='category__tittle',
		to_field_name='tittle')

	class Meta:
		model = Notes
		fields = [
			'category',
		]
