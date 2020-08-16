from django.shortcuts import render

from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def handleSignup(request):
	if request.method == 'POST':

		Username = request.POST['Username']
		emailid = request.POST['emailid']
		password = request.POST['password']
		subjects = request.POST['subjects']
		phonenumber = request.POST['phonenumber']
		

		myuser = User.objects.create_user(username , emailid , password )
		myuser.Username = Username
		myuser.subjects = subjects
		myuser.phonenumber = phonenumber
		myuser.save()
		messages.success(request, "Your account has been successfully created")
		return redirect('/')


	else:
		return HttpResponse("")

def handleLogin(request):
	if request.method == 'POST':

		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request , user)
			messages.success(request, "Successfully logged in")
			return redirect('/')
		else:
			messages.error(request , "Invalid Credentials ,Please try again")
			return redirect('/')

	return HttpResponse('404 - ERROR FOUND')

def handleLogout(request):
	logout(request)
	messages.success(request, "Successfully logged out")
	return redirect('/')


	return HttpResponse('404 - ERROR FOUND')

#def message(request):

