from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class ArchivistLandingView(TemplateView):
    template_name = 'archivist/landing.html'
