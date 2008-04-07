#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, timedelta
from calendar import *

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
