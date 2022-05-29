from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArchivistLandingView.as_view(), name='landing'),
    path('update/<int:pk>', views.ProofArchiveUpdateView.as_view(), name='update'),
    path('<int:pk>', views.ProofArchiveDetailView.as_view(), name='detail'),
]