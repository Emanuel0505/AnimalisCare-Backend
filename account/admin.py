from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("nomeCompleto", "first_name", "last_name", "biografia", "email", "fotoPerfil")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "nomeCompleto", "first_name", "last_name",  "fotoPerfil", "biografia", "cargo"),
        }),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff",)
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)