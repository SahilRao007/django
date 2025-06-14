from django.contrib import admin
from .models import Data
# Register your models here.
class mymodeladmin(admin.ModelAdmin):
    list_display=('title','content')
    
admin.site.register(Data)