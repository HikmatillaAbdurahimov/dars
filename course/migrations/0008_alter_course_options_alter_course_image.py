# Generated by Django 5.0.7 on 2024-07-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['price']},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/course/'),
        ),
    ]
