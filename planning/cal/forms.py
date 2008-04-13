#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.newforms import ModelForm
from models import PlanningSettings, Planning, TypeEvent

class PlanningSettingsForm(ModelForm):
    class Meta:
         model = PlanningSettings
         exclude = ('planning', 'name')
 
class PlanningForm(ModelForm):
    class Meta:
         model = Planning
         exclude = ('user',)

class TypeForm(ModelForm):
    class Meta:
         model = TypeEvent
         exclude = ('user', 'planning')
