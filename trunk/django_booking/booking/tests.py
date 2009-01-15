#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
import calendars

class TestCalendar(TestCase):
    def test_month(self):
        m = calendars.Month(2009, 1)
        print m.days()
    
    def test_year(self):
        print calendars.Year(2009).format()
