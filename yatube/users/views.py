from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm


def SignUp(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return redirect(reverse('users:login'))
    form = RegisterForm()
    return render(request, 'users/signup.html', {'form': form})