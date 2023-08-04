from django.urls import include, path
from rest_framework import routers

from .views import (
    DoctorViewSet,
    ExerciseViewSet,
    PatientViewSet,
    DoctorExerciseViewSet,
)

router = routers.DefaultRouter()
router.register(r"doctors", DoctorViewSet, basename="doctor")
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"exercises", ExerciseViewSet, basename="exercises")
router.register(
    r"doctors/(?P<doctor_id>\d+)/exercises",
    DoctorExerciseViewSet,
    basename="reviews",
)

urlpatterns = [
    path("v1/", include(router.urls)),
]
