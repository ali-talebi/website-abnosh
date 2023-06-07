from django.contrib import admin
from .models import services  
# Register your models here.


@admin.register(services)
class services_admin(admin.ModelAdmin) : 

    list_display = ("name" , "slug" , "status" , "type_service"  )

    search_fields = ("name" ,"slug" )

    list_editabl = ("status" , )

    prepopulated_fields = {'slug' : ("name" , )}  