# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from activity import models
from activity import serializers
# Create your views here.

class IntervalsView(APIView):
    model = None
    serializer = None

    def get(self, request, start, end, format=None):
        try:
            start_dt = datetime.strptime(start, '%Y-%m-%d-%H-%M-%S')
        except ValueError:
            return Response('Start datetime is not valid', status=status.HTTP_400_BAD_REQUEST)
        try:
            end_dt = datetime.strptime(end, '%Y-%m-%d-%H-%M-%S')
        except ValueError:
            return Response('End datetime is not valid', status=status.HTTP_400_BAD_REQUEST)
        if end_dt < start_dt:
            return Response('Start datetime greater than end datetime', status=status.HTTP_400_BAD_REQUEST)
        intervals = self.model.objects.filter(start__lte=start_dt, start__gte=end_dt)
        serializer = self.serializer(intervals, many=True)
        return Response(serializer.data)


class SleepIntervalsView(IntervalsView):
    model = models.Sleep
    serializer = serializers.SleepSerializer


class StepIntervalsView(IntervalsView):
    model = models.Steps
    serializer = serializers.StepSerializer


class PositionIntervalsView(IntervalsView):
    model = models.Position
    serializer = serializers.PositionSerializer
