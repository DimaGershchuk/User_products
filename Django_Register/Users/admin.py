from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department
from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'age', 'gender', 'department')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age', 'gender', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('Add personal info', {
            'fields': ('username', 'email', 'age', 'gender', 'department'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)

