from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ('email', 'company_name', 'register_date',
                    'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    add_fieldsets = (
        (None, {
            'fields': ('email', "company_name", 'password1', 'password2', "is_staff", "is_active", "description")}
         ),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'company_name',)}
         ),
        ("Permissions", {
            'fields': ('is_staff', 'is_active')}
         ),
        ("Personal", {
            'fields': ('description', 'register_date')}
         )
    )
    search_fields = ('email', 'company_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
