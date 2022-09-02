from django.shortcuts import render


def home_page(request):
    return render(request, 'publicPages/index.html')


def about_us_page(request):
    return render(request, 'publicPages/about_us.html')

def contact_us_page(request):
    return render(request, 'publicPages/contact_us.html')


