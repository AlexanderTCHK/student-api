from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CertificatesSerializer
from .models import Certificates


class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
