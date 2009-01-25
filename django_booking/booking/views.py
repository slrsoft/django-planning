#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

import calendars

def display(request, year, template='calendar.html', extra_context={}):
    yeartable = calendars.Year(int(year))
    context = {'yeartable':yeartable,
               'bookables_by_family':ParamFamily.objects.all().order_by('sort_order'),
               'can_edit':True}
    context.update(extra_context)
    response = render_to_response(template, context,
                                  context_instance=RequestContext(request))
    return response

def add_booking(request, days):
    return None

        