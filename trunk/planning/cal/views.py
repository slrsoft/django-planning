#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta

type_vide,c = TypeEvent.objects.get_or_create(name='empty', type='0')

class day:
    def __init__(self, day=None, day_event=None):
        if day:
            self.month = day.month
            self.year, self.week, self.day_week = day.isocalendar()
    

def main(request, template='planning.html'):
    context = {}

    if not request.session.get('user_id', default=False):
        context['user_new']=True
        request.session['user_id'] = request.META['REMOTE_ADDR']
        context['user_state'] = 'init'
    else:
        context['user_state'] = 'alt'
    context['user_id'] = request.session['user_id']
    today = datetime.now().date()
    days = []
    for d in range(10, 0, -1):
        day_date = today - timedelta(days=d)
        if day_date.year < today.year:
            continue
        days.append(day(day_date))
    for d in range(0, 400):
        day_date = today + timedelta(days=d)
        if day_date.year > today.year:
            break
        days.append(day(day_date))
    context['days'] = days
    
    
    return render_to_response(template, context)
