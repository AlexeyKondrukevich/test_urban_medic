from datetime import timedelta

from exercises.models import Doctor, Exercise, ExercisePatient, Patient
from rest_framework.test import APIClient, APITestCase


class DoctorApiTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    def setUp(self):
        Patient.objects.bulk_create(
            [
                Patient(
                    first_name=f"First_Name_{i}", last_name=f"Last_Name_{i}"
                )
                for i in range(3)
            ]
        )
        Doctor.objects.bulk_create(
            [
                Doctor(
                    first_name=f"First_Name_{i}", last_name=f"Last_Name_{i}"
                )
                for i in range(3)
            ]
        )
        self.exercise_first = Exercise.objects.create(
            title="Висы", periodicity=timedelta(days=1)
        )
        self.exercise_first.doctors.add(1)
        self.exercise_second = Exercise.objects.create(
            title="Прыжки", periodicity=timedelta(days=2)
        )
        self.exercise_second.doctors.add(2)
        self.exercise_patient = ExercisePatient.objects.create(
            patient=Patient.objects.get(id=1),
            doctor=Doctor.objects.get(id=1),
            exercise=self.exercise_first,
        )

    def test_create_exercise_patient_by_wrong_doctor(self):
        data = {
            "patient": 1,
            "exercise": 1,
        }
        response = self.client.post("/api/v1/doctors/2/exercises/", data=data)
        error = response.json()["error"]
        massage = "Вы не можете назначить это упражнение. Будьте внимательны."
        self.assertIn(massage, error)

    def test_create_exercise_patient_twice(self):
        data = {
            "patient": 1,
            "exercise": 1,
        }
        response = self.client.post("/api/v1/doctors/1/exercises/", data=data)
        error = response.json()["error"]
        massage = "Пациенту уже назначено это упражнение. Будьте внимательны."
        self.assertIn(massage, error)
