from rest_framework import serializers

from exercises.models import Doctor, Exercise, ExercisePatient, Patient


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
        queryset=Exercise.objects.prefetch_related("doctors").all()
    )

    class Meta:
        model = ExercisePatient
        fields = (
            "patient",
            "exercise",
        )

    def validate(self, data):
        view = self.context.get("view")
        doctor = view.kwargs.get("doctor_id")
        patient = data["patient"]
        exercise = data["exercise"]
        if not exercise.doctors.filter(id=doctor).exists():
            message = (
                "Вы не можете назначить это упражнение. Будьте внимательны."
            )
            raise serializers.ValidationError({"error": message})
        elif ExercisePatient.objects.filter(
            exercise=exercise, patient=patient
        ).exists():
            message = (
                "Пациенту уже назначено это упражнение. Будьте внимательны."
            )
            raise serializers.ValidationError({"error": message})
        return data

    def to_representation(self, instance):
        return ExerciseDoctorSerializer(instance).data


class ExerciseDoctorSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    exercise = ExerciseSerializer()

    class Meta:
        model = ExercisePatient
        fields = "__all__"


class ExercisePatientListSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = ExercisePatient
        fields = "__all__"
