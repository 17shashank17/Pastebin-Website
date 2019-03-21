from django.contrib import admin

# Register your models here.
from .models import RichText,User_Save

admin.site.register(RichText)
admin.site.register(User_Save)
