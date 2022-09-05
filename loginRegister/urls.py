from django.urls import path
from .views import login_page,plans_page,register_page,forget_page


urlpatterns = [
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page'),
    path('forget', forget_page, name='forget_page'),
    path('plans', plans_page, name='plans_page'),

]