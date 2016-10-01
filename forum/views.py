from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse


class HomeView(generic.TemplateView):
  template_name = 'index.html'
