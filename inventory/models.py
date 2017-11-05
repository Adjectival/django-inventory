# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200, null=False, default='New Item')
    description = models.TextField()
    amount = models.IntegerField()
