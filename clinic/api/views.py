from rest_framework import viewsets

from .serializers import DoctorSerializer, PatientSerializer
from exercises.models import Doctor, Patient


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
