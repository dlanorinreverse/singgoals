# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_upload(models.Model):
	musician_name = models.CharField(max_length=250)
	musician_genre = models.CharField(max_length=250)
	musician_contactNumber = models.CharField(max_length=250)
	musician_address = models.CharField(max_length=250)
	musician_email = models.CharField(max_length=250)
	musician_priceRate = models.CharField(max_length=250)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return '{} by {}'.format(self.musician_name, self.musician_email)

#class interactions(models.Model):
#	hired = models.ForeignKey()
#	hiree = models.ForeignKey(User,)