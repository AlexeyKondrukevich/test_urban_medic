from django.db import models


class Doctor(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return " ".join((self.last_name, self.first_name))

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"


class Patient(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return " ".join((self.last_name, self.first_name))

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"


class Exercise(models.Model):
    title = models.CharField("Название", max_length=50, unique=True)
    periodicity = models.DurationField("Периодичность")
    doctors = models.ManyToManyField(
        Doctor, related_name="exercise", verbose_name="Список докторов"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"


class ExercisePatient(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="exercises",
        verbose_name="Пациент",
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        verbose_name="Упражнение",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="exercises_list",
        verbose_name="Доктор",
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата назначения",
    )

    def __str__(self):
        return self.full_title

    @property
    def full_title(self):
        return " || ".join(
            (
                str(self.date),
                str(self.patient),
                str(self.doctor),
                str(self.exercise),
            )
        )

    class Meta:
        verbose_name = "Назначенное упражнение"
        verbose_name_plural = "Назначенные упражнения"
        ordering = ("-date",)
        constraints = [
            models.UniqueConstraint(
                fields=["patient", "exercise"],
                name="unique_patient",
            )
        ]
