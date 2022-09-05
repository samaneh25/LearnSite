from django.shortcuts import render

def login_page(request):
    return render(request, 'loginRegister/login.html')
def register_page(request):
    return render(request, 'loginRegister/register.html')
def forget_page(request):
    return render(request, 'loginRegister/forget.html')
def plans_page(request):
    return render(request, 'loginRegister/plans.html')