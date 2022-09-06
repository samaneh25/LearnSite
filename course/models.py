from django.db import models
from django.conf import settings


class CourseModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    is_single_headline = models.BooleanField()
    video_link = models.CharField(max_length=400)
    description = models.TextField(max_length=1000)
    is_super_course = models.BooleanField()
    teacher_name = models.CharField(max_length=100)


class CourseHeadlinesModel(models.Model):
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class CourseCommentModel(models.Model):
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
