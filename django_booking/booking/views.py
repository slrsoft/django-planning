#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

import calendars
from datetime import date, timedelta

def display(request, year, template='calendar.html', extra_context={}):
    yeartable = calendars.Year(int(year))
    
    yeartable.fill_bookings((Item.objects.get(name='Zone A'),))
    
    context = {'yeartable':yeartable,
               'bookables_by_family':prepare_families(request.session),
               'can_edit':True, 'filter':request.session['filter']}
    context.update(extra_context)
    response = render_to_response(template, context,
                                  context_instance=RequestContext(request))
    return response

def edit(request, year, template='calendar.html', extra_context={}):
    yeartable = calendars.Year(int(year))
    
    yeartable.fill_bookings((Item.objects.get(name='Zone A'),))
    
    context = {'yeartable':yeartable,
               'bookables_by_family':prepare_families(request.session, user=request.user, update_checkboxes=False, edit=True),
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
    datelist = []
    for day in days.split(','):
        y,m,d = day.split('-')
        datelist.append( date(int(y), int(m), int(d)) )
    
    ranges = get_date_ranges(datelist)
    data_object = Item.objects.get(pk=int(id))
    for dmin, dmax in ranges:
        Booking.objects.create(item=data_object,
                                   user=request.user,
                                   start=dmin, end=dmax)
    return HttpResponseRedirect('../../../../')
    #return HttpResponse(str(ranges))

def prepare_families(session, user=None, update_checkboxes=True, edit=False):
    if not session.has_key('filter'):
        session['filter'] = {}
    flist = []
    filter = session['filter']
    
    for f in GroupItem.objects.all().order_by('sort_order'):
        oblist = list(f.item_set.all())
        flist.append({'name':f.name, 'items':oblist})
        if edit and user:
            for ob in oblist:
                ob.editable = ob.is_editable_by(user)
        if update_checkboxes:
            for ob in oblist:
                if filter.has_key(u'%d' % ob.pk):
                    ob.checked = ""
                else:
                    ob.checked = "checked"
    return flist

def get_date_ranges(datelist):
    dmin = datelist[0]
    dmax = dmin
    ranges = []
    j1 = timedelta(days=1)
    for day in datelist[1:]:
        if day == dmax + j1:
            dmax = day
        else:
            ranges.append((dmin, dmax))
            dmin, dmax = day, day
    ranges.append((dmin, dmax))
    return ranges