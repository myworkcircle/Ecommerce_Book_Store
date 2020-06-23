from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UAdmin(UserAdmin):
    list_display = ('email',)
    search_fields = ('email','username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(User,UAdmin)


