from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_active", "is_staff")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ("email", "username", "first_name", "last_name", "is_active")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email", "username", "first_name", "last_name")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2"),
        }),
    )

    ordering = ("email",)
