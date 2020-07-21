# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='')
    date= models.DateField(auto_now=False)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
