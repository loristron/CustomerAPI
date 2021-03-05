from rest_framework import (
					routers,
					serializers,
					viewsets)

from core.models import People


"""
Model serializer setup for the project.
Uses all of the fields from the database

"""
class PeopleSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= People
		fields 	=  (
				'id',
				'first_name',
				'last_name',
				'email',
				'gender',
				'company',
				'city',
				'title',
				'latitude',
				'longitude',
			)