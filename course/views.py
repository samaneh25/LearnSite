from django.shortcuts import render, redirect
from course.models import *
from plan.models import *
from django.contrib.auth.decorators import login_required


def single_course(request, headline_id):
    course = CourseHeadlinesModel.objects.filter(id=headline_id)
    return render(request, 'course/single_course.html', {
        'course': course[0]
    })


def course_preview(request, course_id):
    course_data = CoursePreviewModel.objects.filter(id=course_id)[0]
    headlines = CourseHeadlinesModel.objects.filter(course_id=course_id)
    student_number = SavedCourse.objects.filter(course_id=course_data).count()
    user = request.user
    policy_data = __handle_course_policy(course_data, user)
    # if user is not None:
    #     ans = SavedCourse.objects.filter(user_id=user.id, course_id=course_id).first()
    # else:
    #     ans = None
    # result = True if ans is not None else None

    if request.method == 'POST':
        data = SavedCourse(user_id=request.user, course_id=course_data)
        data.save()
        return redirect('course_preview', course_id)

    return render(request, 'course/course_preview.html', {
        'course_preview': course_data,
        'course_headlines': headlines,
        'policy': policy_data,
        'student_of_this_course_number': student_number,
    })


def __handle_course_policy(course, user):
    result = {}
    if user.is_authenticated:
        if course.is_super_course:
            result['show_super_badge'] = True
            if __has_user_plan_valid(user):
                result['need_plan'] = False
                if __has_user_this_course(user, course):
                    result['show_headlines'] = True
                    result['btn_text'] = 'شما اشتراک این ویدیو را دارید'
                    result['need_register'] = False
                else:
                    result['show_headlines'] = False
                    result['btn_text'] = 'ثبت نام در دوره'
                    result['need_register'] = True
            else:
                result['show_headlines'] = False
                result['need_plan'] = True
                result['btn_text'] = 'برای ثبت نام در این دوره باید اشتراک ویژه یوزرکد را خریداری کنید'
        else:
            if __has_user_this_course(user, course):
                result['show_headlines'] = True
                result['btn_text'] = 'شما در این دوره ثبت نام کرده اید'
                result['need_register'] = False
            else:
                result['show_headlines'] = False
                result['btn_text'] = 'ثبت نام در دوره'
                result['need_register'] = True
    else:
        if course.is_super_course:
            result['show_super_badge'] = False
        result['show_headlines'] = False
        result['show_super_badge'] = False
        result['btn_text'] = 'ابتدا وارد حساب کاربری خود شوید'
        result['need_login'] = True

    return result


def __has_user_plan_valid(user):
    has_plan = UserActivePLan.objects.filter(user_id=user)
    if len(has_plan) != 0 and has_plan[0].is_plan_active:
        return True
    else:
        return False


def __has_user_this_course(user, course):
    user_course = SavedCourse.objects.filter(user_id=user, course_id=course)
    if len(user_course) != 0:
        return True
    else:
        return False
