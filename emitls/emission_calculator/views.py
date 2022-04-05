from django.shortcuts import render, redirect
from django import forms
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import *

# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")


def about(request):
  return render(request, "emission_calculator/about.html")


def options(request):
  return render(request, "emission_calculator/options.html")


def electric(request):
  return render(request, "emission_calculator/electric.html")


def provider(request):
  return render(request, "emission_calculator/provider.html")


def reduce_reuse_recycle(request):
  return render(request, "emission_calculator/rrr.html")


def score(request):
  return render(request, "emission_calculator/score.html", {
        "form": YesNoForm()
    })


def output(request):

  score = 0
  if request.POST['electric_car'] == "True":
    score += 1
    
  if request.POST['provider'] == "True":
    score += 1

  if request.POST['reduce_reuse_recycle'] == "True":
    score += 1

  return render(request, 'emission_calculator/output.html', {
    "number": score,
    "electric": request.POST['electric_car'],
    "provider": request.POST['provider'],
    "rrr": request.POST['reduce_reuse_recycle'],
    "budget": int(request.POST['budget']),
  })

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("calculator:options")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="emission_calculator/signup.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				context = {"user": user}
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, "emission_calculator/account.html", context)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="emission_calculator/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("calculator:")


def my_account(request):
	scores = Score.objects.order_by('user')
	return render(request, "emission_calculator/account.html", {'scores': scores})


def my_account(request):
	scores = Score.objects.order_by('user')
	return render(request, "emission_calculator/account.html", {'scores': scores})