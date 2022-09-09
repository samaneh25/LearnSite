from django.urls import path
from .views import *


urlpatterns = [
    path('plans', plans_page, name='plans_page'),
]