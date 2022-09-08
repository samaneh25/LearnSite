from django.shortcuts import render
from course.models import *
from blog.models import *


def home_page(request):
    newest_blogs = SinglePostModel.objects.all()[:4]
    newest_courses = CoursePreviewModel.objects.filter(is_single_headline=False)[:4]
    single_headline_course = CoursePreviewModel.objects.filter(is_single_headline=True)[:4]
    return render(request, 'publicPages/index.html',
                  {
                      'newest_courses': newest_courses,
                      'single_headline_course': single_headline_course,
                      'newest_blogs': newest_blogs,
                  }
                  )


def about_us_page(request):
    return render(request, 'publicPages/about_us.html')


def contact_us_page(request):
    return render(request, 'publicPages/contact_us.html')
