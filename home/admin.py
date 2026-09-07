from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    ordering = ('email',)  
admin.site.register(User, UserAdmin)
