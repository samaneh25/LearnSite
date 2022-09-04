from django.shortcuts import render


def blog_page(request):
    return render(request, 'blog/blog.html')

def single_blog_page(request):
    return render(request, 'blog/single_blog.html')
