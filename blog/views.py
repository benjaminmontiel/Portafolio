# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog(request):

    blogs = Blog.objects.all()

    return render(request,'blog/blogs.html', {'blogs': blogs })


def detail(request,blog_id):

    blog = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'blog/detail.html', {'blog': blog})
