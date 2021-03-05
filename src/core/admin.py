from django.contrib import admin
from .models import People

#Registrating the People model on the admin setup
admin.site.register(People)