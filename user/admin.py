from django.contrib.admin import ModelAdmin, site

from .models import User


class UserAdmin(ModelAdmin):
    list_display = ['email']

    class Meta:
        model = User

site.register(User, UserAdmin)
