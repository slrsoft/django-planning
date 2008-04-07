#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
from django.utils.dates import WEEKDAYS_ABBR, WEEKDAYS, MONTHS 

class Day:
    def __init__(self, day=None, day_event=None):
        if day:
            self.month = day.month
            self.year, self.week, self.day_week = day.isocalendar()
    def name(self):
        return WEEKDAYS[self.day_week-1]
    def name_abbr(self):
        return WEEKDAYS_ABBR[self.day_week-1]

class Period:
    def __init__(self, day, num):
        self.num = num
        self.day = day
        self.nb = 1
    def incr(self):
        self.nb += 1
    def month_name(self):
        return MONTHS[self.num-1]

class Calendar:
    days = []
    weeks = []
    months = []
    years = []
    def __init__(self, day_start, day_end=None):
        for d in range(0, 400):
            day_date = day_start + timedelta(days=d)
            if not day_end:
                if day_date.year > day_start.year: break
            else:
                if day_date > day_end: break
            day_ob = Day(day_date)
            self.days.append(day_ob)
            self._update_years(day_date, day_date.year)
            self._update_months(day_date, day_date.month)
            self._update_weeks(day_date, day_ob.week)
    
    def _update_years(self, day, year):
        if not self.years: self.years.append(Period(day, year))
        lastyear = self.years[-1]
        if lastyear.num < year:
            self.years.append(Period(day, year))
        else:
            lastyear.incr()
            
    def _update_months(self, day, month):
        if not self.months: self.months.append(Period(day, month))
        lastmonth = self.months[-1]
        if lastmonth.num < month:
            self.months.append(Period(day, month))
        else:
            lastmonth.incr()
            
    def _update_weeks(self, day, week):
        if not self.weeks: self.weeks.append(Period(day, week))
        lastweek = self.weeks[-1]
        if lastweek.num < week:
            self.weeks.append(Period(day, week))
        else:
            lastweek.incr()
