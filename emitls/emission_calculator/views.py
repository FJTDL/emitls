from django.shortcuts import render
from django import forms
from django.http.response import HttpResponseRedirect

class NewTaskForm(forms.Form):
  humanNumber = forms.IntegerField(label="Walk/cycle", min_value=0, max_value=100)
  publicNumber = forms.IntegerField(label="Public transport", min_value=0, max_value=100)
  privateNumber = forms.IntegerField(label="Private vehicle", min_value=0, max_value=100)

# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")


def score(request):
  return render(request, "emission_calculator/score.html", {
        "form": NewTaskForm()
    })