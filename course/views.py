from django.shortcuts import render


def single_course(request):

    return render(request, 'course/course.html')
