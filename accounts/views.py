
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm

@login_required
def edit_profile(request):
	user = request.user
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profil mis à jour avec succès.")
			return redirect('profile')
	else:
		form = UserProfileForm(instance=user)
	return render(request, 'edit-profile.html', {'form': form})
