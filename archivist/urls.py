from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArchivistLandingView.as_view(), name='landing'),
]