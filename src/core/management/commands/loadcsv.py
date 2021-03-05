from django.core.management.base import BaseCommand

import argparse
import csv

from core.models import People


class Command(BaseCommand):
	help = 'Load CSV to models database'

	def add_arguments(self, parser):
		parser.add_argument('--path', type=str)

	def handle(self, *args, **kwargs):
		path 	= kwargs['path']
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
