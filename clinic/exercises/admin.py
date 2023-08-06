from django.contrib import admin

from .models import Doctor, Exercise, ExercisePatient, Patient

admin.site.register(Doctor)
admin.site.register(Exercise)
admin.site.register(Patient)
admin.site.register(ExercisePatient)
