from django.test import TestCase
from .models import People

import csv
import requests


#The setup for this test is to loop through te .csv file and load it on the database 
class PeopleTestCast(TestCase):

	def setUp(self):
		path = 'customers.csv'
		with open(path) as file:
			reader = csv.reader(file)
			#Skip header row
			next(reader, None)  
			
			for row in reader:
				person = People.objects.create(
						pk			= row[0],
						first_name	= row[1],
						last_name	= row[2],
						email		= row[3],
						gender		= row[4],
						company		= row[5],
						city		= row[6],
						title		= row[7],
					)

	#Test case to check if the file loaded properly on the database
	#Expects a number equals to 1000, total rows of the file
	def test_people_loaded(self):
		count 	= People.objects.all().count()
		self.assertEqual(count, 1000)
		self.assertNotEquals(count, 0)

	#Test case to check if the API connection and the object updating is correct
	#Expects not empty fields for Latitude and Longitude
	def test_geocode_loaded(self):
		person		= People.objects.get(pk=1)
		address 	= person.city
		api_key 	= "AIzaSyDAVGI7xnvIIQq5kh6CoWDYXb4kUnVsQRY"
		api_response= requests.get(
			'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
		api_response_dict 	= api_response.json()

		if api_response_dict['status'] == 'OK':
	 		person.latitude  = api_response_dict['results'][0]['geometry']['location']['lat']
	 		person.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
	 		person.save()

		
		self.assertIsNotNone(person.latitude)
		self.assertIsNotNone(person.longitude)


