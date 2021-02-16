from django.contrib import admin
from .models import User,Founder

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'Your_Name','Item_Lost','Description_of_Item','Email','Phone_No','Location_Lost','Date_Lost','Photo', 'Date']

@admin.register(Founder)
class FoundAdmin(admin.ModelAdmin):
    list_display = ['id', 'Your_Name','Item_Found','Description_of_Item','Email','Phone_No','Location_Found','Date_Found','Photo', 'Date']

