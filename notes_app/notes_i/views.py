from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notes
from .forms import CreateNoteForm, UpdateNoteForm
from .filters import NotesFilter


def index(request) -> HttpResponse:
	notes = Notes.objects.all()
	results = NotesFilter(request.GET, queryset=notes)
	context = {'notes': notes, 'results': results}
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
	instance = get_object_or_404(Notes, id=note_id)
	instance.delete()
	return HttpResponseRedirect('/')


def search(request):
	query = request.GET.get('query')
	notes_filtered = Notes.objects.filter(tittle__icontains=query)
	context = {'results': notes_filtered}
	return render(request, 'search.html', context=context)
