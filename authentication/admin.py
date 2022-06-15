from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  NewUser

# class UserAdminConfig(UserAdmin):
#     model = NewUser
#     list_display = ('email', 'user_name', 'first_name','second_name',
#                     'is_active', 'is_staff')
    # ordering = ('-user_name',)
# admin.site.register(NewUser, UserAdminConfig) 
admin.site.register(NewUser)   