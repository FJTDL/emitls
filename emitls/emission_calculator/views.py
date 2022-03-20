from django.shortcuts import render
from django import forms
from django.http.response import HttpResponseRedirect

class NewTaskForm(forms.Form):
  electric_car = forms.IntegerField(label="Do you have an electric vehicle?", min_value=0, max_value=100)
  provider = forms.IntegerField(label="Does your electricity provider generate from renewable sources?", min_value=0, max_value=100)
  reduce_reuse_recycle = forms.IntegerField(label="Do you recycle, reduce and reuse? (score yourself out of 10)", min_value=0, max_value=100)

# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")


def about(request):
  return render(request, "emission_calculator/about.html")


def score(request):
  return render(request, "emission_calculator/score.html", {
        "form": NewTaskForm()
    })


def output(request):
# model closely off of https://github.com/FJTDL/integratedwork/blob/main/site/carbonsite/landing/views.py
  electric = int(request.POST['electric_car'])
  provider = int(request.POST['provider'])
  rrr = int(request.POST['reduce_reuse_recycle'])

  score = electric + provider + rrr

  return render(request, 'emission_calculator/output.html', {
    "score": score
  })