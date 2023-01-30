from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView,RedirectView
class GeekyView(RedirectView):
    url='https://geekyshows.com'