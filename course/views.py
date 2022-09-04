from django.shortcuts import render


def singel_course(request):
    return render(request, 'course/course.html')
