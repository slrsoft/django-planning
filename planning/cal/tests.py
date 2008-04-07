#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest
from django.test.client import Client
from calendar import *
from datetime import date
from models import Profile, Planning
from django.contrib.auth.models import User

class Test(unittest.TestCase):
    def test_calendare(self):
        cal = Calendar(date.today())
        print cal
    
    def test_code(self):
        user = User.objects.create_user('any', 'a@b.fr', 'any')
        p = Profile.objects.create(user=user)
        self.assertEquals(len(p.code), 32, '32 chars code')
        p = Planning.objects.create(user=user, name='plan1', desc='desc')
        self.assertEquals(len(p.code), 32, '32 chars code')
        