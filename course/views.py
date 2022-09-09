from django.shortcuts import render, redirect
from course.models import *
from django.contrib.auth.decorators import login_required


def single_course(request, headline_id):
    course = CourseHeadlinesModel.objects.filter(id=headline_id)
    return render(request, 'course/single_course.html', {
        'course': course[0]
    })


def course_preview(request, course_id):
    course_data = CoursePreviewModel.objects.filter(id=course_id)[0]
    headlines = CourseHeadlinesModel.objects.filter(course_id=course_id)
    student_number = SavedCourse.objects.filter(course_id=course_data).count()
    user = request.user
    if user is not None:
        ans = SavedCourse.objects.filter(user_id=user.id, course_id=course_id).first()
    else:
        ans = None
    result = True if ans is not None else None

    if request.method == 'POST':
        data = SavedCourse(user_id=request.user, course_id=course_data)
        data.save()
        return redirect('course_preview', course_id)

    return render(request, 'course/course_preview.html', {
        'course_preview': course_data,
        'course_headlines': headlines,
        'has_user_this_course': result,
        'student_of_this_course_number': student_number,
    })
