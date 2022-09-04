from django.urls import path
from .views import login_register_page,plans_page


urlpatterns = [
    path('login-register', login_register_page, name='login_register_page'),
    path('plans', plans_page, name='plans_page'),

]