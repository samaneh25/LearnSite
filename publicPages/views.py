from django.shortcuts import render
from course.models import *


def home_page(request):
    newest_courses = CourseModel.objects.all()[:3]
    return render(request, 'publicPages/index.html', {'newest_courses': newest_courses})


def about_us_page(request):
    return render(request, 'publicPages/about_us.html')


def contact_us_page(request):
    return render(request, 'publicPages/contact_us.html')


