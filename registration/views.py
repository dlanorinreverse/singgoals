# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')
	context = {
		'message': 'sign up' 
	}
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = UserCreationForm()
	context['form'] = form
	return render(request, 'sign_up.html', context=context)

def sign_in(request):
	if request.user.is_authenticated:
		return redirect('/')
	context = {
		'message': 'sign in' 
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('/')
		else:
			context['error'] = 'Invalid Username or Password'
			context['username'] = username
	return render(request, 'sign_in.html', context=context)

def sign_out(request):
	logout(request)
	return redirect('/')