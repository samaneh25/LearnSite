from django.db import models
from django.conf import settings
from django.utils.html import escape


class CoursePreviewModel(models.Model):
    title = models.CharField(max_length=100)
    # TODO(model of image)
    # video_cover = models.ImageField(upload_to='course/courseCover', null=True)
    video_cover = models.ImageField(upload_to='media', null=True)

    def admin_image(self):
        return '<img src="%s"/>' % self.video_cover
    admin_image.allow_tags = True
    is_single_headline = models.BooleanField()
    video_link = models.URLField(max_length=400)
    description = models.TextField(max_length=1000)
    is_super_course = models.BooleanField()
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CourseHeadlinesModel(models.Model):
    course_id = models.ForeignKey(CoursePreviewModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField(max_length=400, null=True)
    video_cover = models.ImageField(upload_to='headline', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True)


class CourseCommentModel(models.Model):
    headline_id = models.ForeignKey(CourseHeadlinesModel, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)


class SavedCourse(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CoursePreviewModel, on_delete=models.CASCADE)

