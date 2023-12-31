# Generated by Django 4.2.2 on 2023-08-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('periodicity', models.DurationField(verbose_name='Периодичность')),
                ('doctors', models.ManyToManyField(related_name='exercise', to='exercises.doctor')),
            ],
            options={
                'verbose_name': 'Упражнение',
                'verbose_name_plural': 'Упражнения',
            },
        ),
    ]
