from django.db import models
from django.conf import settings
from django.utils.html import escape


class CourseModel(models.Model):
    title = models.CharField(max_length=100)
    # TODO(model of image)
    video_cover = models.ImageField(upload_to='course/courseCover', null=True)

    def admin_image(self):
        return '<img src="%s"/>' % self.video_cover
    admin_image.allow_tags = True
    is_single_headline = models.BooleanField()
    video_link = models.URLField(max_length=400)
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
