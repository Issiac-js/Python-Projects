from django.contrib import admin

# Register your models here.
from .models import Account, Service
admin.site.register(Account)
admin.site.register(Service)