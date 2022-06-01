from django.contrib import admin

from .models import Car, City, Company
admin.site.register(Car)
admin.site.register(Company)
admin.site.register(City)