from django.contrib import admin
from .models import UserDetail

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email_id')

admin.site.register(UserDetail, UserDetailAdmin)
