from django.urls import path
from publicPages.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about_us', about_us_page, name='about_us_page'),
    path('contact_us', contact_us_page, name='contact_us_page'),

]
