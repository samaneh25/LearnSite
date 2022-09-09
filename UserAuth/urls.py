from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page'),
    path('forget', forget_page, name='forget_page'),
    path('logout', user_logout, name='logout'),

]