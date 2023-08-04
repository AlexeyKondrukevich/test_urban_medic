from exercises.models import Doctor, Exercise, Patient, ExercisePatient
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import (
    DoctorSerializer,
    ExerciseSerializer,
    PatientSerializer,
    ExercisePatientCreateSerializer,
)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class DoctorExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExercisePatient.objects.all()
    serializer_class = ExercisePatientCreateSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        return ExercisePatient.objects.filter(doctor=doctor)

    def perform_create(self, serializer):
        doctor_id = self.kwargs.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        serializer.save(doctor=doctor)
