#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import calendar
from calendar import monthrange

days_ab = ('L', 'M', 'M', 'J', 'V', 'S', 'D')
monthes = (None, u'Janv', u'Fév', u'Mars', u'Avril', u'Mai',
           u'Juin', u'Juill', u'Août', u'Sept', u'Oct', u'Nov', u'Déc')

# hashtable yyyy-mm-dd -> seq of <span color=[data_color]/>
_hash_booking_set = {}

class Day:
    ''' Base class of a day view.
    should be overriden
    '''
    def __init__(self, year, month, daymonth, dayweek):
        self.year, self.month, self.daymonth, self.dayweek = year, month, daymonth, dayweek 
        self.key = '%d-%d-%d' % (self.year, self.month, self.daymonth)
    def tag_id(self):
        return self.key
    def week_end(self):
        return (self.dayweek > 4)
    def span_color_list(self):
        if not _hash_booking_set.has_key(self.key):
            return ""
        return _hash_booking_set[self.key]
    def __str__(self):
        return '%d %s' % (self.daymonth, days_ab[self.dayweek])

class Month:
    def __init__(self, year, month, day_class=Day):
        self.year, self.month, self.day_class = year, month, day_class
    def label(self):
        return monthes[self.month]
    def days(self):
        ''' returns a sequence of days
        '''
        l = []
        d, n = monthrange(self.year, self.month)
        for dm in range(n):
            l.append(self.day_class(self.year, self.month, dm+1, d))
            d = (d+1)%7
        return l

class Year:
    def __init__(self, year, width=6, first_month=1, day_class=Day):
        self.year, self.width, self.first_month, self.day_class = year, width, first_month, day_class
    
    def fill_bookings(self, data_list):
        ''' fills _hash_booking_set
        '''
        for m in range(1,13):
            d, n = monthrange(self.year, m)
            for dm in range(1, n+1):
                key = '%d-%d-%d' % (self.year, m, dm)
                _hash_booking_set[key] = ""
                for data in data_list:
                    _hash_booking_set[key] += data.span_color()
        
    def format(self):
        ''' returns a sequence of sequences of monthes
        '''
        rows = []
        row = (Month(self.year, m+1, self.day_class) for m in range(self.width))
        rows.append(row)
        row = (Month(self.year, m+1, self.day_class) for m in range(self.width, 12))
        rows.append(row)
        return rows