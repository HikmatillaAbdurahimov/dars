# Generated by Django 5.0.7 on 2024-07-18 23:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='active_students',
            field=models.PositiveIntegerField(default=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]