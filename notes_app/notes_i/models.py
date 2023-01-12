from django.db import models


class Category(models.Model):
	tittle = models.CharField(max_length=100)

	def __str__(self):
		return self.tittle

	class Meta:
		verbose_name_plural = "Notes"


class Notes(models.Model):
	tittle = models.CharField(max_length=100)
	text = models.TextField(null=True, blank=True)
	reminder = models.DateTimeField(null=True)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tittle
