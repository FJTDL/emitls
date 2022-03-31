from django.urls import path, include

from . import views

app_name = 'calculator'

urlpatterns = [
  path('', views.home, name=''),
  path('home', views.home, name='home'),
  path('calculator', views.score, name='calculate'),
  path('output', views.output, name='output'),
  path('about', views.about, name='about'),
  path('options', views.options, name='options'),
  path('electric', views.electric, name='electric'),
  path('provider', views.provider, name='provider'),
  path('reduce_reuse_recycle', views.reduce_reuse_recycle, name='reduce_reuse_recycle'),
  path('register', views.register, name='register'),
  path('login', views.login_request, name='login'),
  path('logout', views.logout_request, name='logout'),
]