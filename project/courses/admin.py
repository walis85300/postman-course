from django.contrib import admin

from courses.models import Course, Material, Teacher

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Teacher, TeacherAdmin)
