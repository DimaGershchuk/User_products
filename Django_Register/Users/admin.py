from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product
from .forms import CustomUserCreationForm

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'age', 'gender', 'department')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)

