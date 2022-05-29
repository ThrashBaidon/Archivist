import imp
from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from archivist.forms import ProofArchiveForm
from archivist.models import ProofArchive
from guardian.shortcuts import assign_perm

class ArchivistLandingView(LoginRequiredMixin, TemplateView):
    template_name = 'archivist/landing.html'

class ArchivistViewPermission(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        '''
        Revisa si el el usuario tiene permiso de editar el archivo
        '''
        if self.request.user.has_perm('change_proofarchive', self.get_object()):
            return True

class ArchivisChangetPermission(LoginRequiredMixin, UserPassesTestMixin, FormView):
    def test_func(self):
        '''
        Revisa si el el usuario tiene permiso de editar el archivo
        '''
        if self.request.user.has_perm('change_proofarchive', self.get_object()):
            return True


class ProofArchiveUpdateView(ArchivisChangetPermission, UpdateView):
    model = ProofArchive
    template_name = "archivist/form.html"
    form_class = ProofArchiveForm

    def dispatch(self, request, *args, **kwargs):
        '''
        Si el objeto no existe, lo crea
        '''
        object, created = self.model.objects.get_or_create(pk=kwargs['pk'])
        if created:
            permissions = ['view_proofarchive', 'add_proofarchive', 'change_proofarchive',]
            for permission in permissions:
                assign_perm(permission, request.user, object)
        return super().dispatch(request, *args, **kwargs)


class ProofArchiveDetailView(ArchivistViewPermission, DetailView):
    model = ProofArchive
    