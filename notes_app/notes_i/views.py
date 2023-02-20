from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import CreateNoteForm, UpdateNoteForm
from .filters import NotesFilter
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def index(request):
	if request.user.is_authenticated:
		notes = Notes.objects.filter(author=request.user)
		results = NotesFilter(request.GET, queryset=notes)
		context = {'notes': notes, 'results': results}
	else:
		context = {}
	return render(request, 'index.html', context=context)


@login_required(login_url="/login/")
def create_note(request):
	if request.method == "POST":
		form = CreateNoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.author = request.user
			note.save()
			return HttpResponseRedirect('/')
	else:
		form = CreateNoteForm()
	context = {'form': form}
	return render(request, 'create_note.html', context=context)


@login_required(login_url="/login/")
def update_note(request, note_id):
	instance = get_object_or_404(Notes, id=note_id)
	form = UpdateNoteForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')
	context = {'form': form}
	return render(request, 'update_note.html', context=context)


@login_required(login_url="/login/")
def delete_note(request, note_id):
	instance = get_object_or_404(Notes, id=note_id)
	instance.delete()
	return HttpResponseRedirect('/')


@login_required(login_url="/login/")
def search(request):
	if request.user.is_authenticated:
		query = request.GET.get('query')
		notes_filtered = Notes.objects.filter(tittle__icontains=query, author=request.user)
		context = {'results': notes_filtered}
	else:
		context = {}
	return render(request, 'search.html', context=context)
