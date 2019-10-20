# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
from django.utils import timezone

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=264, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=264)

    #string representation of your model
    def __str__(self):
        return self.name

