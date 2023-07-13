from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

def home(request):
    # check to see if logging in
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have loggen In!")
            return redirect('home')
        else:
            messages.success(request,"There was an Error Logging In, Please try again...")
            return redirect('home')
    else:
        return render(request,'home.html',{})
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Beeen Logged Out....")
    return redirect('home')
# to register user
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

