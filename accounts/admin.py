from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account



# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','phone_number', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined', 'is_active')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
   

admin.site.register(Account, AccountAdmin)