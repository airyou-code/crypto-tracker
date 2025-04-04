from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.model._meta.app_label = 'auth'
