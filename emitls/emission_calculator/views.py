from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "emission_calculator/home.html")