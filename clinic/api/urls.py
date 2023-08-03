from django.urls import include, path
from rest_framework import routers

from .views import DoctorViewSet, PatientViewSet

router = routers.DefaultRouter()
router.register(r"doctors", DoctorViewSet, basename="doctor")
router.register(r"patients", PatientViewSet, basename="patients")

urlpatterns = [
    path("v1/", include(router.urls)),
]
