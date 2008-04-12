#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, timedelta
from calendar import *

from forms import PlanningSettingsForm, PlanningForm

type_vide,c = TypeEvent.objects.get_or_create(name='empty', type='0')

def main(request, template='planning.html'):
    context = {}

    if not request.session.get('user_id', default=False):
        context['user_new']=True
        request.session['user_id'] = request.META['REMOTE_ADDR']
        context['user_state'] = 'init'
    else:
        context['user_state'] = 'alt'
    context['user_id'] = request.session['user_id']
    today = date.today()
    cal = Calendar(today)
    context['cal'] = cal
    
    
    return render_to_response(template, context)

def add_planning(request, redirect='..'):
    if request.method == 'POST':
        form1 = PlanningForm(request.POST)
        form = PlanningSettingsForm(request.POST)
        if form.is_valid():
            # Do form processing here...
            return HttpResponseRedirect(redirect)
    else:
        form1 = PlanningForm()
        form = PlanningSettingsForm()
    return render_to_response('add_planning.html', {'form': form, 'form1': form1})