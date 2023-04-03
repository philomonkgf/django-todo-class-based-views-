from pickle import LIST
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import NewTask
# Register your models here.

# @admin.register(NewTask)
# class NewTaskAdmin(UserAdmin):
#     list_display = ['username','taskname']

admin.site.register(NewTask)