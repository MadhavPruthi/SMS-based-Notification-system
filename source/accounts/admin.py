from django.contrib import admin
from source.accounts.models import Student, Faculty, Course, StudentCourse, FacultyCourse

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(FacultyCourse)
