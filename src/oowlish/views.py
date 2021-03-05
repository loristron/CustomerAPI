from django.shortcuts import (
		get_object_or_404, 
		render, 
		redirect)
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from core.models import People
from .serializers import PeopleSerializer



#List all people saved on the database. 
class PeopleListView(APIView):

	def get(self, request):
		queryset 	= People.objects.all()
		serializer 	= PeopleSerializer(queryset, many=True)
		return Response(serializer.data)

#Based on the PK settend at the endpoit, list that only object
class PeopleDetailView(APIView):

	def get(self, request, pk):
		person 		= get_object_or_404(People, pk=pk)
		serializer 	= PeopleSerializer(person)
		return Response(serializer.data)

#Fill the latitude and logitude fields from the People model with data get from Google Geocode API
def fill_location_fields(request):
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
 	return redirect('schema-swagger-ui')