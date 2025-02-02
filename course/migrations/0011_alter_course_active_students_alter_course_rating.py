# Generated by Django 5.0.7 on 2024-07-18 23:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_active_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='active_students',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
