from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notes
from .forms import CreateNoteForm, UpdateNoteForm


def index(request) -> HttpResponse:
	notes = Notes.objects.all()
	context = {'notes': notes}
	return render(request, 'index.html', context=context)


def create_note(request):

	if request.method == "POST":
		form = CreateNoteForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')
	else:
		form = CreateNoteForm()
	context = {'form': form}
	return render(request, 'create_note.html', context=context)


def update_note(request, note_id):
	instance = get_object_or_404(Notes, id=note_id)
	form = UpdateNoteForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')
	context = {'form': form}
	return render(request, 'update_note.html', context=context)


def delete_note(request, note_id):
	if request.method == "POST":
		instance = get_object_or_404(Notes, id=note_id)
		instance.delete()
		return HttpResponseRedirect('/')
	else:
		form = CreateNoteForm()
	context = {'form': form}
	return render(request, 'create_note.html', context=context)
