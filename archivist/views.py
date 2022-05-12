import imp
from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from archivist.forms import ProofArchiveForm

from archivist.models import ProofArchive

@method_decorator(login_required, name='dispatch')
class ArchivistLandingView(TemplateView):
    template_name = 'archivist/landing.html'

@method_decorator(login_required, name='dispatch')
class ProofArchiveCreateView(CreateView):
    model = ProofArchive
    template_name = "archivist/form.html"
    form_class = ProofArchiveForm

    def form_valid(self, form):
        print('valido')
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProofArchiveUpdateView(UpdateView):
    model = ProofArchive
    template_name = "archivist/form.html"
    form_class = ProofArchiveForm

    def dispatch(self, request, *args, **kwargs):
        '''
        Si el objeto no existe, lo crea
        '''
        self.model.objects.get_or_create(pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ProofArchiveDetailView(DetailView):
    model = ProofArchive
    # template_name = "archivist/form.html"

    