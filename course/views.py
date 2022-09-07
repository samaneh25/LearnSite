from django.shortcuts import render
from course.models import *


def single_course(request, course_id=-1):
    course = CourseModel.objects.filter(id=course_id)
    return render(request, 'course/course.html', {'course': course})
