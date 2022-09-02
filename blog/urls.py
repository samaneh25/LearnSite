from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog', start_page, name='start_page'),
]
