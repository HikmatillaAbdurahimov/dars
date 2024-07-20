from django.shortcuts import render
from course.models import Course,Speciality,Teacher
from blog.models import Blog


def home_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    teachers = Teacher.objects.all()
    blogs = Blog.objects.all()
    context = {
        "courses":courses,
        "specialiys":specialitys,
        "teachers":teachers,
        "blogs":blogs
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def teacher_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    teachers = Teacher.objects.all()
    blogs = Blog.objects.all()
    context = {
        "courses": courses,
        "specialiys": specialitys,
        "teachers": teachers,
        "blogs": blogs
    }
    return render(request, 'teacher.html',context)

def course_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    teachers = Teacher.objects.all()
    blogs = Blog.objects.all()
    context = {
        "courses": courses,
        "specialiys": specialitys,
        "teachers": teachers,
        "blogs": blogs
    }
    return render(request, 'course.html',context)

def blog_view(request):
    return render(request, 'blog.html')


def contact_view(request):
    return render(request, 'contact.html')