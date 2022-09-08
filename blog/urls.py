from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog', blog_page, name='blog_page'),
    path('single_blog/<blog_id>', single_blog_page, name='single_blog_page'),

]
