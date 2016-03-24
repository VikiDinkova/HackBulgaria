from django.shortcuts import render, redirect
from .forms import CourseForm


def home(request):
    return render(request, 'home.html', {})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = CourseForm()
    return render(request, 'add_course.html', {'form': form})
