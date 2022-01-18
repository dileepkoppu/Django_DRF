from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,contact
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets=((None,{'fields':('phone_number','password','name','email')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'email', 'name')
    search_fields = ('name','phone_number', 'email')
    ordering = ('phone_number',)

admin.site.register(User,CustomUserAdmin)

admin.site.register(contact)