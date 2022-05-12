from django import forms

from archivist.models import ProofArchive


class ProofArchiveForm(forms.ModelForm):
    class Meta:
        model = ProofArchive
        exclude = ('user',)
    
    


