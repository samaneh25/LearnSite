from django.urls import path
from .views import login_register_page


urlpatterns = [
    path('login-register', login_register_page, name='login_register_page')
]