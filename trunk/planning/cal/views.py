#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, timedelta

type_vide,c = TypeEvent.objects.get_or_create()

class day:
    day_week
    day_month
    day_event
    def __init__(self, date=None, day_event=None):
         pass
    

def main(request, template='planning.html'):
    context = {}

    if not request.session.get('user_id', default=False):
        context['user_new']=True
        request.session['user_id'] = request.META['REMOTE_ADDR']
        context['user_state'] = 'init'
    else:
        context['user_state'] = 'alt'
    context['user_id'] = request.session['user_id']
    
    
    
    return render_to_response(template, context)
