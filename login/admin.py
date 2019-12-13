from django.contrib import admin

from .models import Profile, quotes


admin.site.register(quotes)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin class."""

    def has_change_permission(self, request, obj=None):
        """Prevent admin from modifying user profile."""
        return False
