from django.shortcuts import render


def login_register_page(request):
    return render(request, 'loginRegister/login_register.html')

def plans_page(request):
    return render(request, 'loginRegister/plans.html')