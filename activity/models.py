# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Interval(models.Model):
    title = models.CharField('Title', max_length=100)
    start = models.DateTimeField('Start time', blank=False, null=False)
    end = models.DateTimeField('End time', blank=False, null=False)
    ordering = models.IntegerField('Ordering', default=0)

    class Meta:
        abstract = True


class Sleep(Interval):
    class Meta:
        verbose_name = 'Sleep'


class Steps(Interval):
    steps = models.PositiveIntegerField('Steps count', default=0)

    class Meta:
        verbose_name = 'Steps'


class Position(Interval):
    latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = 'Position'
