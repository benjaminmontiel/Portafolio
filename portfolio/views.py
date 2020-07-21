# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .models import Project


def portfolio(request):

    projects = Project.objects.all()

    return render (request,'home.html', {'projects': projects})
