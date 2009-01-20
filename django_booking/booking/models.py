from django.db import models
from django.contrib.auth.models import User


class ParamProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    display_order = models.IntegerField()
    name = models.CharField(max_length=300, unique=True, db_column='profile_name')
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'rs_param_profiles'
        verbose_name = 'Profile'

class DataUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    login = models.CharField(unique=True, max_length=60, blank=True)
    profile = models.ForeignKey(ParamProfile, db_column='profile_id')
    email = models.CharField(max_length=240, blank=True)
    password = models.CharField(max_length=60, blank=True)
    locked = models.BooleanField()
    admin = models.BooleanField()
    remarks = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.login
    class Meta:
        db_table = u'rs_data_users'
        verbose_name = 'openbookings user'

class ParamFamily(models.Model):
    family_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()
    name = models.CharField(max_length=150, db_column='family_name')
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'rs_param_families'
        verbose_name = 'Family'
        verbose_name_plural = 'Families'

class Data(models.Model):
    object_id = models.AutoField(primary_key=True)
    rand_code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, db_column='object_name')
    family = models.ForeignKey(ParamFamily)
    manager = models.ForeignKey(DataUser)
    misc_info = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'rs_data_objects'
        verbose_name = 'Bookable object'

class DataBooking(models.Model):
    book_id = models.AutoField(primary_key=True)
    rand_code = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(db_column='book_date')
    data = models.ForeignKey(Data, db_column='object_id', verbose_name='object')
    user = models.ForeignKey(DataUser)
    start = models.DateTimeField(db_column='book_start')
    end = models.DateTimeField(db_column='book_end')
    validated = models.BooleanField()
    misc_info = models.CharField(max_length=765)
    
    def __unicode__(self):
        return self.data.name
    class Meta:
        db_table = u'rs_data_bookings'
        verbose_name = 'Booking'

class Param(models.Model):
    name = models.CharField(max_length=75, primary_key=True, db_column='param_name')
    value = models.CharField(max_length=75, db_column='param_value')
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'rs_param'
        verbose_name = 'Parameter'

class ParamLang(models.Model):
    lang_id = models.AutoField(primary_key=True)
    english = models.CharField(max_length=765, blank=True)
    french = models.CharField(max_length=765, blank=True)
    german = models.CharField(max_length=765, blank=True)
    norwegian = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.english
    class Meta:
        db_table = u'rs_param_lang'
        verbose_name = 'Language parameter'

