# Generated by Django 5.0.7 on 2024-07-17 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 18, 12, 23, 120597), null=True),
        ),
    ]
