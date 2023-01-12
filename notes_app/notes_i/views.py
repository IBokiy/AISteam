from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes, Category


# Create your views here.
def index(request):
	notes = Notes.objects.all()
	# 1. Count notes for all categories.
	# notes_count = Category.objects.count()
	# print(notes_count)
	# 2.
	context = {'notes': notes}
	return render(request, 'index.html', context=context)
