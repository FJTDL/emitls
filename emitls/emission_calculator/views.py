from django.shortcuts import render
from django import forms
from django.http.response import HttpResponseRedirect

class YesNoForm(forms.Form):
    electric_car = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    provider = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    reduce_reuse_recycle = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
                  


# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")


def about(request):
  return render(request, "emission_calculator/about.html")


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
    "score": score
  })