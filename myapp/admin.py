from django.contrib import admin
from  .models import *

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['Company_name','Mob','Email','Customer_id','password','address','Pan_no','GST_no','user_category','customer_category']
    
@admin.register(Master)
class Master(admin.ModelAdmin):
    list_display = ['Name','Email','Mobno','password','created_at']


   
@admin.register(Manager)
class Manager(admin.ModelAdmin):
    list_display = ['username', 'password','Mob','email','user']