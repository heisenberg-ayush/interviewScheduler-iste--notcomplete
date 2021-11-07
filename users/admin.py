from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('full_name', 'reg_num',  'email', 'is_staff', 'is_active',)
    list_filter = ('full_name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'reg_num', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'reg_num', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)