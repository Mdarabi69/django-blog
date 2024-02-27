from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
   
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "age", "phone", "addres")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", 'age')
    search_fields = ("username", "first_name", "last_name", "email")
    fieldsets = UserAdmin.fieldsets + (
        ('سایر اطلاعات', {
            'fields': ('age', 'phone', 'addres',
                
            ),
        }),
    ) 

    