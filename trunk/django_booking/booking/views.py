#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

import calendars

def display(request, year, template='calendar.html', extra_context={}):
    yeartable = calendars.Year(int(year))
    
    yeartable.fill_bookings((Data.objects.get(name='Zone A'),))
    
    context = {'yeartable':yeartable,
               'bookables_by_family':prepare_families(request.session),
               'can_edit':True, 'filter':request.session['filter']}
    context.update(extra_context)
    response = render_to_response(template, context,
                                  context_instance=RequestContext(request))
    return response

def edit(request, year, template='calendar.html', extra_context={}):
    yeartable = calendars.Year(int(year))
    
    yeartable.fill_bookings((Data.objects.get(name='Zone A'),))
    
    context = {'yeartable':yeartable,
               'bookables_by_family':prepare_families(request.session, update_checkboxes=False),
               'can_edit':True, 'filter':request.session['filter']}
    context.update(extra_context)
    response = render_to_response(template, context,
                                  context_instance=RequestContext(request))
    return response

def add_booking(request, days):
    return None

def display_filter(request, year, id, value):
    if not request.session.has_key('filter'):
        request.session['filter'] = {}
    if value=='false':
        request.session['filter'][id] = False
    else:
        del request.session['filter'][id]
    request.session.modified = True

    return HttpResponseRedirect('../../../')
    #return HttpResponse(str(request.session['filter']))

def edit_set(request, year, id, days):
    return HttpResponse(days)

def prepare_families(session, update_checkboxes=True):
    if not session.has_key('filter'):
        session['filter'] = {}
    flist = []
    filter = session['filter']
    
    for f in ParamFamily.objects.all().order_by('sort_order'):
        oblist = list(f.data_set.all())
        flist.append({'name':f.name, 'items':oblist})
        if update_checkboxes:
            for ob in oblist:
                if filter.has_key(u'%d' % ob.pk):
                    ob.checked = ""
                else:
                    ob.checked = "checked"
    return flist