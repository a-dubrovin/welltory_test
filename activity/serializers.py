from rest_framework import serializers

from activity import models


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sleep
        fields = ('id', 'title', 'start', 'end')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sleep
        fields = ('id', 'title', 'start', 'end', 'steps')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sleep
        fields = ('id', 'title', 'start', 'end', 'latitude', 'longitude')
