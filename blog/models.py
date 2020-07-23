# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='static/blog')
    date= models.DateField(auto_now=False)
    url = models.URLField(blank=True)
