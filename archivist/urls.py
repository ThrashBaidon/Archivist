from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArchivistLandingView.as_view(), name='landing'),
    path('files', views.ProofArchiveCreateView.as_view(), name='create'),
    path('files/update/<int:pk>', views.ProofArchiveUpdateView.as_view(), name='update'),
    # path('files/<int:pk>', views.ProofArchiveDetailView.as_view(), name='detail'),
]