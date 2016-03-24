from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    week = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.SlugField()
