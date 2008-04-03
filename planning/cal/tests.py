#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest
from django.test.client import Client

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(1,1,"1=1")