from django.contrib import admin

from .models import Speciality,Course,Teacher

admin.site.register([Speciality,Course,Teacher])
