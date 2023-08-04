from django.contrib import admin

from .models import Doctor, Exercise, Patient, ExercisePatient

admin.site.register(Doctor)
admin.site.register(Exercise)
admin.site.register(Patient)
admin.site.register(ExercisePatient)
