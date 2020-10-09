from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(User, MyUserAdmin)
