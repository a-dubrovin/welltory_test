# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client

from activity import models
# Create your tests here.


class ActivityTestCase(object):
    activity = ''

    def test_bad_url(self):
        c = Client()
        response = c.get('/%s/123456/1233456' % self.activity)
        self.assertEqual(response.status_code, 404)

    def test_start_datetime(self):
        c = Client()
        response = c.get('/%s/2015-05-05-01-61-01/2015-11-05-01-01-01' % self.activity)
        self.assertEqual(response.status_code, 400)

    def test_end_datetime(self):
        c = Client()
        response = c.get('/%s/2015-05-05-01-01-01/2015-11-05-61-01-01' % self.activity)
        self.assertEqual(response.status_code, 400)

    def test_start_datetime_greater(self):
        c = Client()
        response = c.get('/%s/2017-10-05-01-01-01/2015-05-05-01-01-01' % self.activity)
        self.assertEqual(response.status_code, 400)

    def test_empty_response(self):
        c = Client()
        response = c.get('/%s/2015-05-05-01-01-01/2015-11-05-01-01-01' % self.activity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def usual_response(self):
        pass


class SleepTestCase(TestCase, ActivityTestCase):
    activity = 'sleep'

    def setUp(self):
        models.Sleep.objects.create(title='sleep interval 01', start='2015-01-20 01:01:01', end='2015-01-20 01:05:01')
        models.Sleep.objects.create(title='sleep interval 02', start='2015-01-20 01:10:01', end='2015-01-20 01:15:01')
        models.Sleep.objects.create(title='sleep interval 03', start='2015-01-20 02:01:01', end='2015-01-20 01:05:01')

    def usual_response(self):
        c = Client()
        response = c.get('/%s/2015-01-20 01:01:01/2015-01-20 01:11:01' % self.activity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)


class StepTestCase(TestCase, ActivityTestCase):
    activity = 'step'

    def setUp(self):
        models.Steps.objects.create(title='step interval 01', start='2015-01-20 01:01:01', end='2015-01-20 01:05:01', steps=10)
        models.Steps.objects.create(title='step interval 02', start='2015-01-20 01:10:01', end='2015-01-20 01:15:01', steps=20)
        models.Steps.objects.create(title='step interval 03', start='2015-01-20 02:01:01', end='2015-01-20 01:05:01', steps=30)

    def usual_response(self):
        c = Client()
        response = c.get('/%s/2015-01-20 01:01:01/2015-01-20 01:11:01' % self.activity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['steps'], 10)
        self.assertEqual(response.json()[0]['steps'], 20)


class PositionTestCase(TestCase, ActivityTestCase):
    activity = 'position'

    def setUp(self):
        models.Position.objects.create(title='position interval 01', start='2015-01-20 01:01:01', end='2015-01-20 01:05:01', latitude=37.617409, longitude=54.192630)
        models.Position.objects.create(title='position interval 02', start='2015-01-20 01:10:01', end='2015-01-20 01:15:01', latitude=37.590286, longitude=54.178535)
        models.Position.objects.create(title='position interval 03', start='2015-01-20 02:01:01', end='2015-01-20 01:05:01', latitude=37.597496, longitude=54.171385)

    def usual_response(self):
        c = Client()
        response = c.get('/%s/2015-01-20 01:01:01/2015-01-20 01:11:01' % self.activity)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['latitude'], 37.617409)
        self.assertEqual(response.json()[0]['longitude'], 54.192630)
