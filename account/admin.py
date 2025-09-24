from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("nomeCompleto", "nomeautoridade", "biografia", "email", "fotoPerfil")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "nomeCompleto", "nomeautoridade", "fotoPerfil", "biografia", "cargo"),
        }),
    )
    list_display = ("username", "email", "nomeCompleto", "nomeautoridade", "is_staff",)
    search_fields = ("username", "email", "nomeCompleto", "nomeautoridade")
    ordering = ("username",)