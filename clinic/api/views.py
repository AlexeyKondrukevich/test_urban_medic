from exercises.models import Doctor, Exercise, Patient, ExercisePatient
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404

from .serializers import (
    DoctorSerializer,
    ExerciseSerializer,
    PatientSerializer,
    ExercisePatientCreateSerializer,
    ExercisePatientListSerializer,
)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.prefetch_related("doctors").all()
    serializer_class = ExerciseSerializer


class DoctorExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExercisePatient.objects.select_related(
        "patient", "exercise", "doctor"
    ).all()
    serializer_class = ExercisePatientCreateSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        return ExercisePatient.objects.select_related(
            "patient", "exercise", "doctor"
        ).filter(doctor=doctor)

    def perform_create(self, serializer):
        doctor_id = self.kwargs.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        serializer.save(doctor=doctor)


class PatientExerciseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ExercisePatient.objects.select_related(
        "patient", "exercise", "doctor"
    ).all()
    serializer_class = ExercisePatientListSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get("patient_id")
        patient = get_object_or_404(Patient, id=patient_id)
        return ExercisePatient.objects.filter(patient=patient)
