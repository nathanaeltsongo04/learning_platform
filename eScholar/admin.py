from django.contrib import admin
from . models import *

@admin.register(CompteUtilisateur)
class TabClient(admin.ModelAdmin):
    list_display=['last_name','first_name','username','email','password']