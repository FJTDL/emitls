from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('calculator', views.score, name='calculate'),
  path('output', views.output, name='output'),
  path('about', views.about, name='about'),
  path('options', views.options, name='options'),
  path('electric', views.electric, name='electric'),
  path('provider', views.provider, name='provider'),
  path('reduce_reuse_recycle', views.reduce_reuse_recycle, name='reduce_reuse_recycle'),
  path('signup', views.SignUp.as_view(), name='signup'),
]