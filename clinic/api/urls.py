from django.urls import include, path
from rest_framework import routers

from .views import (
    DoctorViewSet,
    ExerciseViewSet,
    PatientViewSet,
    DoctorExerciseViewSet,
    PatientExerciseViewSet,
)

router = routers.DefaultRouter()
router.register(r"doctors", DoctorViewSet, basename="doctor")
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"exercises", ExerciseViewSet, basename="exercises")
router.register(
    r"doctors/(?P<doctor_id>\d+)/exercises",
    DoctorExerciseViewSet,
    basename="doctors_exercises",
)
router.register(
    r"patients/(?P<patient_id>\d+)/exercises-list",
    PatientExerciseViewSet,
    basename="patients_exercises_list",
)

urlpatterns = [
    path("v1/", include(router.urls)),
]
