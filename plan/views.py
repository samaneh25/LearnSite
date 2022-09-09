from django.shortcuts import render, redirect
from .models import *


def plans_page(request):
    message = ""
    plans = PlanModel.objects.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            selected_plan = PlanModel.objects.filter(id=request.POST['plan_id']).first()
            user_plan = UserActivePLan.objects.filter(user_id=request.user, plan_id=selected_plan, is_plan_active=True)
            if len(user_plan) != 0:
                message = 'این اشتراک برای شما فعال است'
            else:
                UserActivePLan(user_id=request.user, plan_id=selected_plan, is_plan_active=True,
                               remain_date=calculate_remain_days(selected_plan.period)).save()
                message = 'اشتراک با موفقیت برای شما فعال شد :)'
                return render(request, 'plan/plans.html', {'plans': plans, 'message': message})
        else:
            message = 'ابتدا وارد حساب کاربری خود شوید'
            # return redirect('plans_page', {'message': message})

    return render(request, 'plan/plans.html', {'plans': plans, 'message': message})


def calculate_remain_days(period):
    if period == '۱ ماهه':
        return 30
    elif period == '۳ ماهه':
        return 60
    elif period == '۶ ماهه':
        return 120
