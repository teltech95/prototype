from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
 
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
      (1, 'technician'),
      (2, 'agronomy'),
      (3, 'hod'),
    )
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default= 1)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True) 
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff'), default=False) 
    #national_id = models.CharField(max_length=15,  null=True, blank=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return str(self.phone)

    class Meta:
        db_table = "users"

class District(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')


    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "districts"

class Farmer(models.Model):
    GENDER_TYPE_CHOICES = (
      (1, 'male'),
      (2, 'female'),
      (3, 'other'),
    )
    district = models.PositiveIntegerField()
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    physical_address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True) 
    gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE_CHOICES, default= 3)

    class Meta:
        verbose_name = _('farmer')
        verbose_name_plural = _('farmers')


    def __str__(self):
        return str(self.last_name)

    class Meta:
        db_table = "farmers"

class Variable(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('variable')
        verbose_name_plural = _('variables')


    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "variables"

#group or level model
class LGroup(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    variable_id = models.TextField(null=True)  #list 1, 2 and more

    class Meta:
        verbose_name = _('lgroup')
        verbose_name_plural = _('lgroup')


    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "lgroup"

class History(models.Model):
    description = models.TextField(max_length=500, null=True, blank=True)
    createdAt = models.DateTimeField(_('date created'), auto_now_add=True)
    class Meta:
        verbose_name = _('history')
        verbose_name_plural = _('histories')

    class Meta:
        db_table = "histories"

class TestedSample(models.Model):
    sample_size = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    farmerid = models.IntegerField()
    historyid = models.IntegerField()
    groupid = models.IntegerField()
    reading = models.CharField(max_length=100, blank=True, null=True)#reading from machine
    result = models.CharField(max_length=100, blank=True, null=True)#acidic, 
    recommendation = models.TextField(max_length=200, blank=True, null=True)
    approved = models.BooleanField(default=False)
    approved_by = models.IntegerField(blank=True, null=True)#user id
    createdAt = models.DateTimeField(_('date created'), auto_now_add=True)

    class Meta:
        verbose_name = _('sample')
        verbose_name_plural = _('samples')


    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "samples"



#views.py
# import json

# model = 'Paym_doc'
# search = '123456'
# list_id = [1, 3, 8]
# search_id = Main_search.objects.create(name=search, list_id=json.dumps(list_id), model=model).id

# #*
# jsonDec = json.decoder.JSONDecoder()
# rec = Main_search.objects.get(id=search_id)
# list_id = jsonDec.decode(rec.list_id)