#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from random import choice
import string
def gen_string(length=32, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='utilisateur', unique=True, edit_inline=True, max_num_in_admin=1, num_in_admin=1)
    manager = models.BooleanField(default=False, core=True)
    code = models.CharField(max_length=50, editable=False, unique=True, verbose_name='code')
    
    def save(self):
        if not self.code:
            self.code = gen_string()
        models.Model.save(self)
    
    class Admin:
        pass

class TypeEvent(models.Model):
    file = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=1, choices=(('0','vide'),('1','congé'),), default='0')
    
    def graphic(self):
        if not self.file: return ''
        return '<img name=image%d src=%s>' % (self.id, self.get_file_url())
    graphic.allow_tags=True
    
    class Admin:
        list_display = ('name', 'graphic', 'type')
    def __unicode__(self):
        return self.name

class DayEvent(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    valid_user = models.ForeignKey(User, null=True, blank=True, related_name='valid_dayevent_set')
    type = models.ForeignKey(TypeEvent)
    day = models.DateField()
    class Admin:
        list_display = ('user', 'day', 'type', 'valid_user')

class Planning(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='name')
    desc = models.TextField(verbose_name='description')
    code = models.CharField(max_length=50, verbose_name='code')
    
    def save(self):
        if not self.code:
            self.code = gen_string()
        models.Model.save(self)
    
    def __unicode__(self):
        return self.name
    class Admin:
        list_display = ('name','user')
