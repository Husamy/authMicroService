from django.contrib import admin

from authuser.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)