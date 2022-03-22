from django.shortcuts import render
from django import forms
from django.http.response import HttpResponseRedirect
from colorama import Fore

class YesNoForm(forms.Form):
    electric_car = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    provider = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    reduce_reuse_recycle = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))


# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")


def about(request):
  return render(request, "emission_calculator/about.html")


def options(request):
  return render(request, "emission_calculator/options.html")


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

  if score <= 1:
    output = "Bad"
  elif score == 2:
    output = "Ok"
  elif score == 3:
    output = "Good"
  else:
    output = "How"

  # if output == "Bad":
  #   output = Fore.RED + output
  # elif output == "Ok":
  #   output = Fore.BLUE + output
  # elif output == "Good":
  #   output = Fore.GREEN + output
  # else:
  #   pass


  return render(request, 'emission_calculator/output.html', {
    "number": score,
    "rating": output
  })