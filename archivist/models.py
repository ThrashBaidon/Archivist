from django.db import models
from django.urls import reverse

# Create your models here.
'''
documentos necesarios:
1 comprobante de PTC
2 comprobante de nombramiento de postgrado en UPE
3.a comprobante de Docencia una asignatura curricular (4 horas a la semana) durante los ciclos 2021, 2020
y 2019

3.b comrpobante de Generación o aplicación innovadora del conocimiento/investigación
    aplicada, asimilación, desarrollo y transferencia de
    tecnología/innovación, investigación aplicada y desarrollo tecnológico

        Productos válidos que serán considerados:
        ➢ Libros y Capítulos de libro
        ➢ Artículos arbitrados y artículos indexados
        ➢ Artículos arbitrados y artículos indexados:
        ➢ Modelos de utilidad.
        ➢ Patentes.
        ➢ Prototipos.
        ➢ Transferencia de tecnología.
        ➢ Desarrollo de infraestructura
        ➢ Informes Técnicos
        ➢ Obras artísticas:
'''

class ProofArchive(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, primary_key=True)
    ptc_proof = models.FileField(upload_to='proofs', null=True)
    graduate_proof = models.FileField(upload_to='proofs', null=True)
    teaching_proof = models.FileField(upload_to='proofs', null=True)
    knowledge_proof = models.FileField(upload_to='proofs', null=True)

    @property
    def status(self):
        if self.ptc_proof and self.graduate_proof and self.teaching_proof and self.knowledge_proof:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
    
    