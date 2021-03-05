from django.db import models
import requests


# Create your models here.
class People(models.Model):
	first_name 		= models.CharField(max_length=200, null=True)
	last_name		= models.CharField(max_length=200, null=True)
	email			= models.EmailField(null=True)
	gender 			= models.CharField(max_length=30, null=True)
	company			= models.CharField(max_length=200, null=True)
	city			= models.CharField(max_length=200, null=True)
	title			= models.CharField(max_length=200, null=True)

	latitude		= models.CharField(max_length=200, null=True)
	longitude 		= models.CharField(max_length=200, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'