from django.urls import path
from course.views import *

urlpatterns = [
    path('singel_course/<headline_id>', single_course, name='single_course'),
    path('course_preview/<course_id>', course_preview, name='course_preview'),
]
