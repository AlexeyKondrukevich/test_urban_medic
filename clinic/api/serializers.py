from exercises.models import Doctor, Patient, Exercise, ExercisePatient
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    doctors = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), many=True
    )

    class Meta:
        model = Exercise
        fields = "__all__"

    def create(self, validated_data):
        doctors = validated_data.pop("doctors")
        exercise = super().create(validated_data)
        exercise.doctors.set(doctors)
        return exercise

    def update(self, obj, validated_data):
        if "doctors" in validated_data:
            doctors = validated_data.pop("doctors")
            obj.doctors.clear()
            obj.doctors.set(doctors)
        return super().update(obj, validated_data)


class ExercisePatientCreateSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all()
    )
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all()
    )

    class Meta:
        model = ExercisePatient
        fields = (
            "patient",
            "exercise",
        )
