from django.core.management.base import BaseCommand
import requests

from core.models import People


class Command(BaseCommand):
	help = 'Fill the lagitude and longitude of the empty rows from the database People '

	def handle(self, *args, **kwargs):
		queryset	= People.objects.filter(latitude__isnull=True, longitude__isnull=True)
		for obj in queryset:
			address = obj.city
			api_key = "AIzaSyDAVGI7xnvIIQq5kh6CoWDYXb4kUnVsQRY"
			api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
			api_response_dict = api_response.json()
			if api_response_dict['status'] == 'OK':
		 		obj.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
		 		obj.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
		 		obj.save()   
