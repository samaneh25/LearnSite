from django.urls import path
from course.views import *

urlpatterns = [
    path('singel_course/<course_id>', single_course, name='single_course'),
]
