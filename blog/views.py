from django.shortcuts import render
from .models import *


def blog_page(request):
    blogs = SinglePostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': blogs})


def single_blog_page(request, blog_id):
    blog = SinglePostModel.objects.filter(id=blog_id)[0]
    return render(request, 'blog/single_blog.html', {'post': blog})
