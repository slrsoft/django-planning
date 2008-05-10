#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import DayEvent, TypeEvent
from django.contrib.auth.models import User
from datetime import date, timedelta
from calendar import *

from forms import PlanningSettingsForm, PlanningForm, TypeForm
from models import Planning, PlanningSettings, TypeEvent, gen_string

type_vide,c = TypeEvent.objects.get_or_create(name='empty', type='0')

def main(request, template='planning.html'):
    context = {}
    context['user_id'] = init_user(request)
    
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
            p.user = get_user(request)
            p.save()
            pset = form.save(commit=False)
            pset.planning = p
            pset.save()
            request.session['planning_code'] = p.code
            redirect = redirect % p.id
            return HttpResponseRedirect(redirect)
    else:
        form1 = PlanningForm()
        form = PlanningSettingsForm()
    return render_to_response('add_planning.html', {'form': form, 'form1': form1, 'user_id':request.session['user_id']})


def edit(request, id, template='edit.html', redirect='..'):
    p = Planning.objects.get(id=int(id))
    if p.user != get_user(request):
        raise Exception('Not authorized.')
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


def planning(request, code=None, template='planning.html'):
    context = {}
    if not code:
        code=request.session['planning_code']
    else:
        request.session['planning_code'] = code
    p = Planning.objects.get(code=code)
    types = TypeEvent.objects.all()
    today = date.today()
    cal = Calendar(today)
    context['cal'] = cal
    context['types'] = types
    context['blank'] = TypeEvent.objects.get(name='empty')
    user = get_user(request)
    context['user_id'] = user.username
    return render_to_response(template, context)

def get_user(request):
    user_id = init_user(request)
    luser = User.objects.filter(username=user_id)
    if luser.count()==0:
        return User.objects.create_user(user_id, '')
    else:
        return luser[0]

def init_user(request):
    if not request.session.get('user_id', default=False):
        request.session['user_id'] = gen_string()
    return request.session['user_id']
    