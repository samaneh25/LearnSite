from django.shortcuts import render
from course.models import *


def single_course(request, headline_id):
    course = CourseHeadlinesModel.objects.filter(id=headline_id)
    return render(request, 'course/single_course.html', {
        'course': course[0]
    })


def course_preview(request, course_id):
    course_data = CoursePreviewModel.objects.filter(id=course_id)[0]
    headlines = CourseHeadlinesModel.objects.filter(course_id=course_id)
    return render(request, 'course/course_preview.html', {
        'course_preview': course_data,
        'course_headlines': headlines,
    })
