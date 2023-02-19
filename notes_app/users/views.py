from django.contrib.auth import login
from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.
def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
		return HttpResponseRedirect('/')
	else:
		form = SignUpForm()
	return render(request, 'registration/sign_up.html', context={'form': form})
