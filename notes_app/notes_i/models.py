from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	tittle = models.CharField(max_length=100)

	objects = models.Manager()

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tittle

	def __repr__(self):
		return f'Category object: {self.tittle}'


class Notes(models.Model):
	tittle = models.CharField(max_length=100, verbose_name='Note')
	text = models.TextField(null=True, blank=True)
	reminder = models.CharField(max_length=100, null=True, blank=True)
	create_date = models.DateField(auto_now_add=True, verbose_name='Create date')
	update_date = models.DateField(auto_now=True, verbose_name='Update date')
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, verbose_name='Category', blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=1)

	objects = models.Manager()

	class Meta:
		verbose_name = "Note"
		verbose_name_plural = "Notes"

	def __str__(self):
		return self.tittle

	def __repr__(self):
		return f'Note object: {self.tittle}'
