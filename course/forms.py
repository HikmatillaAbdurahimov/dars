from django import forms
from .models import Course,Teacher

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description','image', 'mentor', 'price', 'rating']

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'rating', 'active_students']


