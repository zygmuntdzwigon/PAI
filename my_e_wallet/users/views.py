from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView, DeleteView
from .mixins import UserIsModeratorMixin


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User created successfully for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

    return render(request, 'users/profile.html', context)

def permission_denied(request, exception):
    return render(request, 'users/403.html')

def invalid(request, exception):
    return render(request, 'users/404.html')

@login_required
def pw_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your password was changed successfully!')
            logout(request)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change.html', { 'form': form})


class UsersListView(LoginRequiredMixin, UserIsModeratorMixin, ListView):
    model = User
    ordering = ['username']
    context_object_name = 'users'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserDeleteView(LoginRequiredMixin, UserIsModeratorMixin, DeleteView):
    model = User
    success_url = '/admin'