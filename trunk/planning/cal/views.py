#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, timedelta
from calendar import *

from forms import PlanningSettingsForm, PlanningForm, TypeForm
from models import Planning, PlanningSettings, TypeEvent

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
            p = form1.save(commit=False)
            p.user = request.user
            p.save()
            pset = form.save(commit=False)
            pset.planning = p
            pset.save()
            redirect = redirect % p.id
            return HttpResponseRedirect(redirect)
    else:
        form1 = PlanningForm()
        form = PlanningSettingsForm()
    return render_to_response('add_planning.html', {'form': form, 'form1': form1})


def edit(request, id, template='edit.html', redirect='..'):
    p = Planning.objects.get(id=int(id))
    pset = PlanningSettings.objects.get(planning=p, name='default')
    types = TypeEvent.objects.all()
    if request.method == 'POST':
        form1 = PlanningForm(request.POST, instance=p)
        form = PlanningSettingsForm(request.POST, instance=pset)
        if form.is_valid() and form1.is_valid():
            # Do form processing here...
            return HttpResponseRedirect(redirect)
    else:
        form1 = PlanningForm(instance=p)
        form = PlanningSettingsForm(instance=pset)
    return render_to_response(template, {'form': form,
                                         'form1': form1,
                                         'planning_url':'http://%s/planning/%s/' % (request.META['HTTP_HOST'], p.code),
                                         'types':types})

def add_type(request, id, template='type.html', redirect='../edit/'):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            # Do form processing here...
            return HttpResponseRedirect(redirect)
    else:
        form = TypeForm()
    return render_to_response(template, {'form': form})


def planning(request, code, template='planning.html'):
    context = {}
    p = Planning.objects.get(code=code)
    types = TypeEvent.objects.all()
    today = date.today()
    cal = Calendar(today)
    context['cal'] = cal
    context['types'] = types
    return render_to_response(template, context)
