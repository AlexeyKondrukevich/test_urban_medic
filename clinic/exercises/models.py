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
