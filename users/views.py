from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.http import Http404
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(
                username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticate_user)
            return redirect('forum:home')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile_view(request):
    context = {'user': request.user}
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method != 'POST':
        form = EditProfileForm(instance=request.user)
    else:
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('users:profile')

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)


@login_required
def change_password(request):

    if request.method != 'POST':
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            changed_user = form.save()
            update_session_auth_hash(request, changed_user.user)
            return redirect('users/profile')

    context = {'form': form}
    return render(request, 'users/change_password.html', context)
