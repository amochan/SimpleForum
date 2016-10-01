from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, SignupForm
from .models import UserProfile


def login_view(request):
  if request.method == 'GET':
    form = LoginForm()
    context = { 'form': form }
    return render(request, 'login.html', context)

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if not form.is_valid():
      context = { 'form': form }
      return render(request, 'login.html', context)

  username = form.cleaned_data['username']
  password = form.cleaned_data['password']
  user = authenticate(username=username, password=password)
  print(user)
  login(request, user)
  return HttpResponseRedirect(reverse('home'))

@login_required
def logout_view(require):
  logout(require)
  return HttpResponseRedirect(reverse('home'))

def signup_view(request):
  if request.method == 'GET':
    form = SignupForm()
    context = { 'form': form }
    return render(request, 'signup.html', context)

  if request.method == 'POST':
    form = SignupForm(request.POST)
    if not form.is_valid():
      context = { 'form': form }
      return render(request, 'signup.html', context)
    
  data = form.cleaned_data
  if User.objects.filter(username=data['email']).exists():
    context = { 'form': form }
    return render(request, 'signup.html', context)

  username = data['username']
  password = data['password']
  email = data['email']
  user = User.objects.create_user(username=username, password=password, email=email)

  profile = UserProfile(user)
  user = authenticate(username=username, password=password)
  login(request, user)
  return HttpResponseRedirect(reverse('home'))
