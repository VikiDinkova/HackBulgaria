from django.contrib import admin
from .models import Course, Lecture


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'start_date',
        'end_date'
    )

    class Meta:
        model = Course

admin.site.register(Course, CourseAdmin)


class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'week',
        'course',
        'url'
    )

    class Meta:
        model = Lecture

admin.site.register(Lecture, LectureAdmin)
