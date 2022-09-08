from django.contrib import admin
from .models import *


@admin.register(CourseModel)
class CourseModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_single_headline', 'is_super_course', 'teacher_name']


@admin.register(CourseHeadlinesModel)
class CourseHeadlinesModel(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'title']


@admin.register(CourseCommentModel)
class CourseCommentModel(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'user_id', 'comment']
