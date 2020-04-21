from django.contrib import admin
from profiles.models import Profile

# Register your models here.
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from profiles.models import Profile
from profiles.forms import ProfileChangeForm, ProfileCreationForm

"""
Custom user model admin page
"""


class ProfileAdmin(UserAdmin):
    """
    Fields used to update an existing user
    """

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("name", "photo", "frontend", "backend", "year_started_learning", "company",)},
        ),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    """
    Fields used to create a new user profile
    """
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "photo",
                    "frontend",
                    "backend",
                    "year_started_learning",
                    "company",
                ),
            },
        ),
    )
    form = ProfileChangeForm
    add_form = ProfileCreationForm
    list_display = ("email", "name", "is_staff")
    search_fields = ("email", "name")
    ordering = ("email",)


admin.site.register(Profile, ProfileAdmin)
