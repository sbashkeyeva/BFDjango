from django.contrib import admin

# Register your models here.

from .models import Human,Todo

admin.site.register(Human)
admin.site.register(Todo)
