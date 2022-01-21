from django.contrib import admin
from .models import Pruser

# Register your models here.

class PruserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    
admin.site.register(Pruser, PruserAdmin)