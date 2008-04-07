#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest
from django.test.client import Client
from calendar import *
from datetime import date

class Test(unittest.TestCase):
    def test_calendare(self):
        cal = Calendar(date.today())
        print cal