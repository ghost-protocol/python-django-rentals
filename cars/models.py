from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Cartype(models.Model):
	type = models.CharField(max_length=200)

	def __unicode__(self):
		return self.type

class Car(models.Model):
	type = models.ForeignKey(Cartype)
	name = models.CharField(max_length=200)
	manufacturer = models.CharField(max_length=200)
	engine = models.CharField(max_length=20)

	def __unicode__(self):
		return("%s %s" % (self.manufacturer, self.name))

class Location(models.Model):
	city = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __unicode__(self):
		return("%s %s" % (self.city, self.address))

class Client(models.Model):
	username = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	age = models.IntegerField()
	email = models.EmailField(max_length=254)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=100)

	def __unicode__(self):
		return("%s %s" % (self.firstname, self.lastname))

class Order(models.Model):
	username = models.ForeignKey(Client)
	# user = models.ForeignKey('auth.User')
	car = models.ForeignKey(Car)
	pickup_time = models.DateTimeField(default=timezone.now)
	dropoff_time = models.DateTimeField(default=timezone.now)
	pickup_location = models.ForeignKey(Location, related_name='order_pickup_locations')
	dropoff_location = models.ForeignKey(Location, related_name='order_dropoff_locations')
	created = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return("%s %s" % (self.car, self.pickup_time))
