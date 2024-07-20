from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from course.models import Speciality
from .forms import BlogForm,BlogUpdateForm
from django.http import HttpResponse

def blog_view(request):
    blogs = Blog.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'blog.html', {"blogs":blogs, "specialitys":specialitys})


def blog_detail_view(request, id):
    blog = Blog.objects.all(id=id)
    specialitys = Speciality.objects.all()
    return render(request, 'blog-detail.html', {'blog':blog})


def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')

    form = BlogForm()
    return render(request, 'blog_create.html', {'form':form})


def blog_update_view(request,pk):
    blogs = get_object_or_404(Blog, pk=pk)
    if request.method =="POST":
        form = BlogUpdateForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', pk=blogs.pk)
        else:
            form = BlogUpdateForm()
            return render(request, "blog_update.html", {'blogs': blogs,"message_error":'Error', 'blogs':blogs})

    blogs = Blog.objects.get(pk=pk)
    return render(request, "blog_update.html", {'blogs':blogs})


def blog_delete_view(request,id):
    blogs = Blog.object.get(id=id)
    blogs.delete()
    return redirect('blog-list')
