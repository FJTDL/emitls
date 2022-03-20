from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('calculator', views.score, name='calculate'),
  path('output', views.output, name='output'),
  path('about', views.about, name='about'),
]