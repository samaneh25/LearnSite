from course.models import CoursePreviewModel


def courses_list(request):
    courses = CoursePreviewModel.objects.all()
    return {'menu_courses': courses}
