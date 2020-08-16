from django.shortcuts import render

from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from twilio.rest import Client

def home(request):
	print('inside home')
	return render(request,'index.html')


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

def messageWhatsapp(subject,title,msg):
    account_sid = 'ACf8092d44602f315fd319e1a618b341c9'
    auth_token = 'c87ba5203f4a78c4a612f8be98f3778d'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=msg,
    from_='whatsapp:+14155238886',
                     to='whatsapp:+919833040567',
                 )

def message(subject,title,msg):
    account_sid = 'ACf8092d44602f315fd319e1a618b341c9'
    auth_token = 'c87ba5203f4a78c4a612f8be98f3778d'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=msg,
                    from_='+12512929449',
            to='+919833040567'
                 )
def sendmessage(request):
    subject = request.POST.get('subject')
    title = request.POST.get('title')
    msg = request.POST.get('message')
    message(subject,title,message)
    messageWhatsapp(subject,title,message)

